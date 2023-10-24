import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET
import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class SubirSrchivoGUI(customtkinter.CTk):
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
        label_datos_generales = customtkinter.CTkLabel(frame_1, text="Datos Generales", font=customtkinter.CTkFont(size=30, weight="bold"), text_color="#0f4e9c")
        label_datos_generales.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        
        # Crear un CTkTabview para agregar pestañas
        self.tabview = customtkinter.CTkTabview(master=frame_1, width=300)
        self.tabview.pack(pady=20, padx=60, fill="x", expand=True)
        
        # Agregar pestañas
        self.tabview.add("Subir XML")
        self.tabview.add("Visualizar XML")
        
        #Tabview 1
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Subir XML"), text="Cargar archivo", command=self.uploadFile)
        self.string_input_button.pack(pady=20, padx=60, expand=True)
        
        #Tabview 2
        self.label = customtkinter.CTkLabel(self.tabview.tab("Visualizar XML"), text="Por favor, subir XML", font=customtkinter.CTkFont(size=20) )
        self.label.pack(pady=20, padx=60, expand=True)
        self.textbox = customtkinter.CTkTextbox(self.tabview.tab("Visualizar XML"), width=250)
        self.textbox.configure(state="disabled")
    
    #Funcion para subir un archivo
    def uploadFile(self):
        global file_path, xml_data
        file_path = askopenfilename(filetypes=[("XML files", "*.xml")])
        if file_path:
            xml_data = self.parse_xml(file_path)
            if xml_data is not None:
                
                #Editando el textbox para mostrar datos
                self.textbox.configure(state="normal")
                self.textbox.delete(1.0, tkinter.END)
                self.textbox.pack(pady=20, padx=60, fill="x", expand=True)
                self.textbox.insert(tkinter.END, ET.tostring(xml_data, encoding="unicode"))
                self.textbox.configure(state="disabled")
                
                #Quitar label
                self.label.pack_forget()
                messagebox.showinfo("Carga de archivo completa", "El archivo se ha cargado correctamente.")
        else:
            pass
    
    #Analizando XML
    def parse_xml(self, file_path):
        try:
            tree = ET.parse(file_path)
            return tree.getroot()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo analizar el archivo XML:\n{str(e)}")
            return None

if __name__ == "__main__":
    app = SubirSrchivoGUI()
    app.mainloop()