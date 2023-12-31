import tkinter
import json
import os
import customtkinter


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class AgregarRegimen(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Datos Generales")
        self.geometry(f"{1100}x{580}")

        def guardar_json():
            data = {}
            route = "../ProyectoContaduria-main/datos"
            os.makedirs(route, exist_ok=True)

            route = os.path.join(route, "datos.json")
            if os.path.exists(route):
                with open(route, "r") as f:
                    data = json.load(f)

            nuevo_regimen = {
                "Nombre": self.nombre.get(),
                "Numero del regimen": self.numero_regimen.get()
            }
            data[len(data) + 1] = nuevo_regimen

            with open(route, "w") as f:
                json.dump(data, f, indent=4)

        self.guardar_json = guardar_json

        def aceptar():
            self.guardar_json()

        # Crear un frame superior de color azul
        top_frame = tkinter.Frame(self, bg="#0f4e9c", height=60)
        top_frame.pack(fill="x")

        frame_1 = customtkinter.CTkFrame(self)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        ################################################################################################
        #Creacion de elementos
        ################################################################################################

        # Crear labels
        label_datos_generales = customtkinter.CTkLabel(frame_1, text="Agregar nuevo regimen fiscal", font=customtkinter.CTkFont(size=30, weight="bold"),
                                                        text_color="#0f4e9c")
        label_nombre = customtkinter.CTkLabel(frame_1, text="Nombre", font=customtkinter.CTkFont(size=20) )
        label_numero_regimen = customtkinter.CTkLabel(frame_1, text="Número",font=customtkinter.CTkFont(size=20))
        #label_direccion = customtkinter.CTkLabel(frame_1, text="Dirección", font=customtkinter.CTkFont(size=20))
        #label_regimen = customtkinter.CTkLabel(frame_1, text="Regimen",font=customtkinter.CTkFont(size=20))
        #label_ejercicio = customtkinter.CTkLabel(frame_1, text="Ejercicio", font=customtkinter.CTkFont(size=20))

        # Crear las entradas de texto
        self.nombre = customtkinter.CTkEntry(frame_1,
                                            width=400,
                                            height=35,
                                            placeholder_text="Nombre del regimen")
        self.numero_regimen = customtkinter.CTkEntry(frame_1, 
                                          width=400,
                                          height=35,
                                          placeholder_text="Número del regimen")
        #self.direccion = customtkinter.CTkEntry(frame_1, 
        #                                        width=400,
        #                                        height=35,
        #                                        placeholder_text="Dirección de la empresa")
        #self.regimen = customtkinter.CTkEntry(frame_1, 
        #                                      width=400,
        #                                      height=35,
        #                                      placeholder_text="")
        #self.ejercicio = customtkinter.CTkEntry(frame_1, 
        #                                        width=400,
        #                                        height=35,
        #                                        placeholder_text="Año")
        
        #Buton para continuar a la siguiente pantalla
        #Aun no tiene eventos
        self.aceptar = customtkinter.CTkButton(frame_1, text="Aceptar", command = aceptar)
        self.cancelar = customtkinter.CTkButton(frame_1, text="Cancelar")

        #self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                       command=self.change_scaling_event)
        
        ################################################################################################
        #Posicionamiento
        ################################################################################################

        #Se posicionan los labels a lado de su respectiva entrada
        label_datos_generales.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        label_nombre.place(relx=0.35, rely=0.2, anchor=tkinter.CENTER)
        label_numero_regimen.place(relx=0.35, rely=0.3, anchor=tkinter.CENTER)
        #label_numero_regimen.place(relx=0.35, rely=0.3, anchor=tkinter.CENTER)
        #label_direccion.place(relx=0.35, rely=0.4, anchor=tkinter.CENTER)
        #label_regimen.place(relx=0.35, rely=0.5, anchor=tkinter.CENTER)
        #label_ejercicio.place(relx=0.35, rely=0.6, anchor=tkinter.CENTER)

        #Colocar las entardas de texto en el centro de la pantalla
        #Con rely se ajusta que queden una debajo de la otra con el porcentaje de la pantalla
        self.nombre.place(relx=0.6, rely=0.2, anchor=tkinter.CENTER)
        self.numero_regimen.place(relx=0.6, rely=0.3, anchor=tkinter.CENTER)
        #self.numero_regimen.place(relx=0.6, rely=0.3, anchor=tkinter.CENTER)
        #self.direccion.place(relx=0.6, rely=0.4, anchor=tkinter.CENTER)
        #self.regimen.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)
        #self.ejercicio.place(relx=0.6, rely=0.6, anchor=tkinter.CENTER)


        
        #Se coloca el boton en el centro del eje X pero debajo del ultimo entry siendo el 0.8 de la pantalla
        self.aceptar.place(relx=0.35, rely=0.8, anchor=tkinter.CENTER)
        self.cancelar.place(relx=0.65, rely=0.8, anchor=tkinter.CENTER)

        #self.scaling_optionemenu.place(relx=0.7, rely=0.8, anchor=tkinter.CENTER)
        def change_scaling_event(self, new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            customtkinter.set_widget_scaling(new_scaling_float)


if __name__ == "__main__":
    app = AgregarRegimen()
    app.mainloop()