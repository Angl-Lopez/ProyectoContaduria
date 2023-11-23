import os
import customtkinter
from tkinter import filedialog
from openpyxl import load_workbook
import webbrowser
import tkinter

class RevisarGUI(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        
        label_datos_generales = customtkinter.CTkLabel(self, text="Revisar y Guardar reporte", font=customtkinter.CTkFont(size=30, weight="bold"),
                                                       text_color="#0f4e9c")
        
        label_datos_generales.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        # Agrega el botón
        self.btn_visualizar_editar = customtkinter.CTkButton(
            self,
            text="Visualizar Reporte",
            command=self.visualizar_editar_xlsx
        )
        self.btn_visualizar_editar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def visualizar_editar_xlsx(self):
        # Ruta al archivo xlsx
        ruta_xlsx = "CFDIs.xlsx"

        # Verifica si el archivo existe
        if os.path.exists(ruta_xlsx):
            # Intenta abrir el archivo con la aplicación predeterminada
            try:
                os.startfile(ruta_xlsx)  # Abre el archivo con la aplicación predeterminada
            except Exception as e:
                print(f"No se pudo abrir el archivo: {e}")
        else:
            print("El archivo CFDIs.xlsx no existe en la ruta especificada.")

