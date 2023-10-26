import tkinter
import customtkinter
import json
import pandas as pd

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class EmpresaGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Datos Generales")
        self.geometry(f"{1100}x{580}")

        # Crear un frame superior de color azul
        top_frame = tkinter.Frame(self, bg="#0f4e9c", height=60)
        top_frame.pack(fill="x")

        frame_1 = customtkinter.CTkFrame(self)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        ################################################################################################
        #Creacion de elementos
        ################################################################################################

        # Crear labels
        label_datos_generales = customtkinter.CTkLabel(frame_1, text="Datos Generales", font=customtkinter.CTkFont(size=30, weight="bold"),
                                                        text_color="#0f4e9c")
        label_nombre = customtkinter.CTkLabel(frame_1, text="Nombre", font=customtkinter.CTkFont(size=20) )
        label_rfc = customtkinter.CTkLabel(frame_1, text="RFC",font=customtkinter.CTkFont(size=20))
        label_direccion = customtkinter.CTkLabel(frame_1, text="Dirección", font=customtkinter.CTkFont(size=20))
        label_regimen = customtkinter.CTkLabel(frame_1, text="Regimen",font=customtkinter.CTkFont(size=20))
        label_ejercicio = customtkinter.CTkLabel(frame_1, text="Ejercicio", font=customtkinter.CTkFont(size=20))



        data = pd.read_json("./datos/regimenes.json", orient="index")

        data["Concatenado"] = data["Numero del regimen"] + " " + data["Nombre"]
        values_concatenados = data["Concatenado"].tolist()

        # Crear las entradas de texto
        self.nombre = customtkinter.CTkEntry(frame_1,
                                            width=400,
                                            height=35,
                                            placeholder_text="Nombre de la empresa")
        self.rfc = customtkinter.CTkEntry(frame_1, 
                                         width=400,
                                          height=35,
                                          placeholder_text="RFC de la empresa")

        self.direccion = customtkinter.CTkEntry(frame_1, 
                                                width=400,
                                                height=35,
                                                placeholder_text="Dirección de la empresa")
        self.regimen = customtkinter.CTkOptionMenu(frame_1,
                                                    width=400,
                                                    height=35,
                                                    values=values_concatenados)
        self.ejercicio = customtkinter.CTkEntry(frame_1, 
                                                width=400,
                                                height=35,
                                                placeholder_text="Año")
        
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(frame_1, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(frame_1, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)

        #Buton para continuar a la siguiente pantalla
        #Aun no tiene eventos
        self.continuar = customtkinter.CTkButton(frame_1, text="Continuar")

        self.guardar = customtkinter.CTkButton(frame_1, text="Guardar datos", command= self.guardar_datos)

        self.editar_regimen = customtkinter.CTkButton(frame_1, text="Editar Regimen", command= self.editar_regimenes)
        
        ################################################################################################
        #Posicionamiento
        ################################################################################################

        #Se posicionan los labels a lado de su respectiva entrada
        label_datos_generales.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        label_nombre.place(relx=0.35, rely=0.2, anchor=tkinter.CENTER)
        label_rfc.place(relx=0.35, rely=0.3, anchor=tkinter.CENTER)
        label_direccion.place(relx=0.35, rely=0.4, anchor=tkinter.CENTER)
        label_regimen.place(relx=0.35, rely=0.5, anchor=tkinter.CENTER)
        label_ejercicio.place(relx=0.35, rely=0.6, anchor=tkinter.CENTER)

        #Colocar las entardas de texto en el centro de la pantalla
        #Con rely se ajusta que queden una debajo de la otra con el porcentaje de la pantalla
        self.nombre.place(relx=0.6, rely=0.2, anchor=tkinter.CENTER)
        self.rfc.place(relx=0.6, rely=0.3, anchor=tkinter.CENTER)
        self.direccion.place(relx=0.6, rely=0.4, anchor=tkinter.CENTER)
        self.regimen.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)
        self.ejercicio.place(relx=0.6, rely=0.6, anchor=tkinter.CENTER)

        
        #Se coloca el boton en el centro del eje X pero debajo del ultimo entry siendo el 0.8 de la pantalla
        self.continuar.place(relx=0.4, rely=0.8, anchor=tkinter.CENTER)
        self.guardar.place(relx=0.6, rely=0.8, anchor=tkinter.CENTER)
        self.editar_regimen.place(relx=0.8, rely=0.8, anchor=tkinter.CENTER)


        self.appearance_mode_optionemenu.place(relx=0.1, rely=0.9, anchor=tkinter.CENTER)
        self.scaling_optionemenu.place(relx=0.1, rely=0.8, anchor=tkinter.CENTER)
    
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def getterNombre(self):
        return self.nombre.get()

    def getterRfc(self):
        return self.rfc.get()

    def getterDireccion(self):
        return self.direccion.get()

    def getterRegimen(self):
        return self.regimen.get()

    def getterEjercicio(self):
        return self.ejercicio.get()

    
    def guardar_datos(self):
        # Obtener los valores de los campos Entry utilizando las funciones getter
        nombre_empresa = self.getterNombre()
        rfc_empresa = self.getterRfc()
        direccion_empresa = self.getterDireccion()
        regimen_empresa = self.getterRegimen()
        ejercicio_empresa = self.getterEjercicio()

        # Crear una instancia de la clase GetData y pasar los valores
        save_data   = SaveData()
        data        = GetData(nombre_empresa, rfc_empresa, direccion_empresa, regimen_empresa, ejercicio_empresa)
        datos       = data.getData()  # Imprimir los datos (puedes reemplazar esto con tu lógica de almacenamiento)
        save_data.saveData(datos)

    def editar_regimenes(self):
        import subprocess
        subprocess.Popen(["python", "app\EditarRegimenGUI.py"])

class GetData:
    def __init__(self, nombre, rfc, direccion, regimen, ejercicio):
        self.nombre     = nombre
        self.rfc        = rfc
        self.direccion  = direccion
        self.regimen    = regimen
        self.ejercicio  = ejercicio


    def getData(self):

        data = {
            "nombre"    : self.nombre,
            "rfc"       : self.rfc,
            "direccion" : self.direccion,
            "regimen"   : self.regimen,
            "ejercicio" : self.ejercicio
        }

        return data

class SaveData:
    def saveData(self, data):
        #../ProyectoContaduria-main/datos
        file_path = "datos/EmpresaDatos.json"
        with open(file_path, "w") as json_file:
            json.dump(data, json_file)
