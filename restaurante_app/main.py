import tkinter as tk
from pathlib import Path


from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import loginview
from ui.main_view import MainView


class RestauranteApp:
    # Organiza la ventana y conecta las partes de la aplicacion.
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Restaurante App - tkinter")
        self.root.geometry("900x650")
        self.root.minsize(700, 550)

        # Prepara los servicios que usara en la vista principal y en el login.
        ruta_base = Path(__file__).resolve().parent
        archivo_servicio = ArchivoServicio(ruta_base / "datos")
        self.restaurante_servicio = RestauranteServicio(archivo_servicio)

        self.configurar_icono_ventana(ruta_base)
        self.vista_actual = None
        self.mostrar_login()

    def configurar_icono_ventana(self, ruta_base):
        # Coloca el icono de la aplicacion en la ventana.
        ruta_icono = ruta_base / "assets" / "logo" / "icono.png"
        if not ruta_icono.exists():
            return

        try:
            self.icono_app = tk.PhotoImage(file=str(ruta_icono))
            self.root.iconphoto(True, self.icono_app)
        except tk.TclError:
            pass


    def cambiar_vista(self, nueva_vista):
        # Oculta la vista anterior y muestra la nueva.
        if self.vista_actual is not None:
            self.vista_actual.pack_forget()

        self.vista_actual = nueva_vista
        self.vista_actual.pack(fill="both", expand=True)

    def mostrar_login(self):
        # Abre la pantalla para iniciar sesion.
        vista = loginview(self.root, self.restaurante_servicio, self.mostrar_interfaz_principal)
        self.cambiar_vista(vista)

    def mostrar_interfaz_principal(self, usuario_actual):
        # Abre el menu principal despues de validar al usuario.
        vista = MainView(self.root, self.restaurante_servicio, usuario_actual, self.mostrar_login)
        self.cambiar_vista(vista)

    def ejecutar(self):
        # Mantiene la ventana abierta y atenta a los botones.
        self.root.mainloop()


if __name__ == "__main__":
    app = RestauranteApp()
    app.ejecutar()
