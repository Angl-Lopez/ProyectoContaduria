import tkinter as tk
import customtkinter
import json
import pandas as pd

class EmpresaGUI(customtkinter.CTkFrame):
    def __init__(self, parent, datos_empresa):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        # Etiquetas
        label_datos_generales = customtkinter.CTkLabel(self, text="Datos Generales", font=customtkinter.CTkFont(size=30, weight="bold"),
                                                       text_color="#0f4e9c")
        labels = [
            customtkinter.CTkLabel(self, text="Nombre", font=customtkinter.CTkFont(size=20)),
            customtkinter.CTkLabel(self, text="RFC", font=customtkinter.CTkFont(size=20)),
            customtkinter.CTkLabel(self, text="Dirección", font=customtkinter.CTkFont(size=20)),
            customtkinter.CTkLabel(self, text="Regimen", font=customtkinter.CTkFont(size=20)),
            customtkinter.CTkLabel(self, text="Ejercicio", font=customtkinter.CTkFont(size=20)),
        ]

        label_datos_generales = customtkinter.CTkLabel(self, text="Datos Generales", font=customtkinter.CTkFont(size=30, weight="bold"),
                                                       text_color="#0f4e9c")
        label_nombre = customtkinter.CTkLabel(self, text="Nombre", font=customtkinter.CTkFont(size=20))
        label_rfc = customtkinter.CTkLabel(self, text="RFC", font=customtkinter.CTkFont(size=20))
        label_direccion = customtkinter.CTkLabel(self, text="Dirección", font=customtkinter.CTkFont(size=20))
        label_regimen = customtkinter.CTkLabel(self, text="Regimen", font=customtkinter.CTkFont(size=20))
        label_ejercicio = customtkinter.CTkLabel(self, text="Ejercicio", font=customtkinter.CTkFont(size=20))

        # Datos
        data = pd.read_json("./datos/regimenes.json", orient="index")
        data["Concatenado"] = data["Numero del regimen"] + " " + data["Nombre"]
        values_concatenados = data["Concatenado"].tolist()

        # Entradas y botones
        self.nombre = customtkinter.CTkEntry(self, width=400, height=35, placeholder_text="Nombre de la empresa")
        self.rfc = customtkinter.CTkEntry(self, width=400, height=35, placeholder_text="RFC de la empresa")
        self.direccion = customtkinter.CTkEntry(self, width=400, height=35, placeholder_text="Dirección de la empresa")
        self.regimen = customtkinter.CTkOptionMenu(self, width=400, height=35, values=values_concatenados)
        self.ejercicio = customtkinter.CTkEntry(self, width=400, height=35, placeholder_text="Año")

        # Botones adicionales
        self.continuar = customtkinter.CTkButton(self, text="Continuar")
        self.guardar = customtkinter.CTkButton(self, text="Guardar datos", command=self.guardar_datos)
        self.editar_regimen = customtkinter.CTkButton(self, text="Editar Regimen", command=self.editar_regimenes)

        label_datos_generales.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        label_nombre.place(relx=0.25, rely=0.2, anchor=tk.CENTER)
        label_rfc.place(relx=0.25, rely=0.3, anchor=tk.CENTER)
        label_direccion.place(relx=0.25, rely=0.4, anchor=tk.CENTER)
        label_regimen.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
        label_ejercicio.place(relx=0.25, rely=0.6, anchor=tk.CENTER)

        entries = [self.nombre, self.rfc, self.direccion, self.regimen, self.ejercicio]
        for i, entry in enumerate(entries):
            entry.place(relx=0.55, rely=0.2 + i * 0.1, anchor=tk.CENTER)

        buttons = [self.continuar, self.guardar, self.editar_regimen]
        for i, button in enumerate(buttons):
            button.place(relx=0.30 + i * 0.2, rely=0.8, anchor=tk.CENTER)

        # Rellenar datos iniciales
        self.nombre.insert(0, datos_empresa["nombre"])
        self.rfc.insert(0, datos_empresa["rfc"])
        self.direccion.insert(0, datos_empresa["direccion"])
        self.ejercicio.insert(0, datos_empresa["ejercicio"])

        # Establecer la referencia de la aplicación
        self.set_app_reference(parent)

    def set_app_reference(self, app):
        self.app = app

    def guardar_datos(self):
        nombre_empresa = self.getterNombre()
        rfc_empresa = self.getterRfc()
        direccion_empresa = self.getterDireccion()
        regimen_empresa = self.getterRegimen()
        ejercicio_empresa = self.getterEjercicio()

        save_data = SaveData()
        data = GetData(nombre_empresa, rfc_empresa, direccion_empresa, regimen_empresa, ejercicio_empresa)
        datos = data.getData()
        save_data.saveData(datos)
        self.app.guardar_datos()

    def editar_regimenes(self):
        import subprocess
        subprocess.Popen(["python", "app/EditarRegimenGUI"])
        self.app.editar_regimenes()



class GetData:
    def __init__(self, nombre, rfc, direccion, regimen, ejercicio):
        self.nombre = nombre
        self.rfc = rfc
        self.direccion = direccion
        self.regimen = regimen
        self.ejercicio = ejercicio

    def getData(self):
        data = {
            "nombre": self.nombre,
            "rfc": self.rfc,
            "direccion": self.direccion,
            "regimen": self.regimen,
            "ejercicio": self.ejercicio
        }
        return data


class SaveData:
    def saveData(self, data):
        file_path = "datos/EmpresaDatos.json"
        with open(file_path, "w") as json_file:
            json.dump(data, json_file)