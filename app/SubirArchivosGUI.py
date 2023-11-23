import tkinter
from tkinter import messagebox, filedialog, Listbox
import xml.etree.ElementTree as ET
import customtkinter
import os
import glob
import shutil

class SubirArchivosGUI(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
    
        # Crear labels
        label_datos_generales = customtkinter.CTkLabel(self, text="XML", font=customtkinter.CTkFont(size=30, weight="bold"), text_color="#0f4e9c")
        label_datos_generales.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        
        # Crear un CTkTabview para agregar pestañas
        self.tabview = customtkinter.CTkTabview(master=self, width=300)
        self.tabview.pack(pady=20, padx=60, fill="x", expand=True)
        
        # Agregar pestañas
        self.tabview.add("Subir Archivos XML")
        self.tabview.add("Mostrar contenido")
        
        # Tabview 1
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Subir Archivos XML"), text="Seleccionar Carpeta", command=self.uploadFile)
        self.string_input_button.pack(pady=20, padx=60, expand=True)
        
        # Tabview 2
        self.label = customtkinter.CTkLabel(self.tabview.tab("Mostrar contenido"), text="Por favor, subir XML", font=customtkinter.CTkFont(size=20))
        self.label.pack(pady=20, padx=60, expand=True)
        self.xml_listbox = Listbox(self.tabview.tab("Mostrar contenido"))
    
    def set_app_reference(self, app):
        self.app = app

    # Función para subir un archivo
    def uploadFile(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            # Crear una nueva carpeta en el directorio del programa para guardar los archivos XML
            program_directory = os.path.dirname(os.path.realpath(__file__))
            self.new_folder_path = os.path.join(program_directory, "XML")
            os.makedirs(self.new_folder_path, exist_ok=True)

            xml_files = glob.glob(os.path.join(folder_path, '*.xml'))
            self.xml_listbox.delete(0, tkinter.END)
            for file in xml_files:
                # Copiar cada archivo XML a la nueva carpeta
                new_file_path = shutil.copy(file, self.new_folder_path)
                # Añadir el archivo al Listbox
                self.xml_listbox.insert(tkinter.END, os.path.basename(new_file_path))

            self.xml_listbox.pack(padx=20, pady=20, expand=True)
            self.label.pack_forget()
            messagebox.showinfo("Carga de archivos completa", "Los archivos se han cargado correctamente.")
        else:
            pass
        #self.app.uploadFile()