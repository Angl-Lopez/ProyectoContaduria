import os
import xml.etree.ElementTree as ET
import pandas as pd
import xlsxwriter

class CFDIProcessor:
    def __init__(self):
        self.data = []
        self.detalle_data = []  # Agrega esta línea
        self.total_ingresos = 0
        self.total_egresos = 0
        self.total_iva = 0
        self.tipo = None

    def process_cfdi(self, cfdi, tipo):
        # Analiza el XML
        root = ET.fromstring(cfdi)
        
        # Encuentra los nodos necesarios
        emisor_node = root.find(".//cfdi:Emisor", namespaces={'cfdi': 'http://www.sat.gob.mx/cfd/4'})
        receptor_node = root.find(".//cfdi:Receptor", namespaces={'cfdi': 'http://www.sat.gob.mx/cfd/4'})
        concepto_node = root.find(".//cfdi:Conceptos/cfdi:Concepto", namespaces={'cfdi': 'http://www.sat.gob.mx/cfd/4'})

        # Obtiene los datos necesarios
        emisor_rfc = emisor_node.attrib.get('rfc', '')
        receptor_rfc = receptor_node.attrib.get('rfc', '')
        concepto = concepto_node.attrib.get('descripcion', '')
        nombre_emisor = emisor_node.attrib.get('nombre', '')
        nombre_receptor = receptor_node.attrib.get('nombre', '')

        # Obtener la fecha, el IVA y el total
        fecha = root.attrib.get('fecha')
        iva = root.find('.//cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado', namespaces={'cfdi': 'http://www.sat.gob.mx/cfd/4'}).attrib.get('importe')
        total = root.attrib.get('total')

        # Almacena los datos generales
        self.data.append({
            'Fecha': fecha,
            'Total': total,
            'IVA': iva,
            'Tipo': tipo
        })

        # Almacena los datos detallados
        # Almacena los datos detallados
        self.detalle_data.append({
            'Emisor_RFC': emisor_rfc,
            'Receptor_RFC': receptor_rfc,
            'Concepto': concepto,
            'Nombre_Emisor': nombre_emisor,
            'Nombre_Receptor': nombre_receptor,
            'Tipo': self.tipo,
        })

        # Convertir las variables a tipo numérico antes de sumar
        total = float(total)
        iva = float(iva)

        # Suma a los totales
        if tipo == 'Ingreso':
            self.total_ingresos += total
        elif tipo == 'Egreso':
            self.total_egresos += total
        self.total_iva += iva

    def calculate_isr(self, total_ingresos, tipo):
        # Calcula la base del ISR
        base_isr = total_ingresos - self.total_egresos

        # Calcula el ISR 
        isr = base_isr * 0.15

        return isr

    def save_to_excel(self, filename):
        # Crea un DataFrame de pandas con los datos generales
        df_general = pd.DataFrame(self.data)

        # Crea un DataFrame de pandas con los datos detallados
        df_detalles = pd.DataFrame(self.detalle_data)

        # Guarda ambos DataFrames en hojas separadas del archivo de Excel
        with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
            df_general.to_excel(writer, sheet_name='Resumen', index=False)
            df_detalles.to_excel(writer, sheet_name='Detalles', index=False)


    def process_folder(self, folder):
        # Recorre todos los archivos en la carpeta
        for filename in os.listdir(folder):
            # Solo procesa los archivos XML
            if filename.endswith('.xml'):
                # Determina el tipo de CFDI basándose en el nombre del archivo
                tipo = 'Ingreso' if 'ingreso' in filename else 'Egreso'
                self.tipo = tipo
                
                # Abre el archivo y lee el contenido
                with open(os.path.join(folder, filename), 'r') as file:
                    cfdi = file.read()
                
                # Procesa el CFDI
                self.process_cfdi(cfdi, tipo)


