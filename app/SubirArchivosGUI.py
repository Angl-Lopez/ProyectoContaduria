import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class SubirSrchivoGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Datos Generales")
        self.geometry(f"{1100}x{580}")

if __name__ == "__main__":
    app = SubirSrchivoGUI()
    app.mainloop()