import customtkinter
from EmpresaGUI import EmpresaGUI

class General(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Datos Generales")
        self.geometry(f"{1100}x{580}")

        self.tabview = customtkinter.CTkTabview(self, width=1100, height=580)
        self.tabview.add("Inicio")
        self.tabview.add("Subir XML")
        self.tabview.add("Descargar Reporte")

        # Crear una instancia de EmpresaGUI y agregarla al tab "Inicio"
        empresa_gui = EmpresaGUI(self.tabview.tab["Inicio"])
        empresa_gui.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = General()
    app.mainloop()
