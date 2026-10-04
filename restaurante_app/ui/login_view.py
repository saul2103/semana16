from pathlib import Path
import tkinter as tk
from tkinter import ttk


class loginview(tk.Frame):
    # Muestra el formulario para entrar a la aplicacion.
    def __init__(self, master, restaurante_servicio, al_inicar_sesion):
        super().__init__(master)
        self.restaurante_servicio = restaurante_servicio
        self.al_inicar_sesion = al_inicar_sesion

        self.usuario_entry = None
        self.contrasena_entry = None
        self.mensaje_error = None

        self.definir_estilos()
        self.construir_interfaz()

    def cargar_logo(self):
        # Busca el logo y lo prepara para mostrarlo arriba.
        ruta_base = Path(__file__).resolve().parent.parent
        ruta_logo = ruta_base / "assets" / "logo" / "restaurante.png"

        if not ruta_logo.exists():
            return None

        logo_original=tk.PhotoImage(file=str(ruta_logo))
        self.logo = logo_original.subsample(3, 3)
        return self.logo
    


    def definir_estilos(self):
        # Define la apariencia del boton de entrada.
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "Login.TButton",
            background="#2563eb",
            foreground="#ffffff",
            font=("Arial", 11, "bold"),
            padding=(14, 8),
            borderwidth=0,
        )
        estilo.map("Login.TButton", background=[("active", "#1d4ed8")])

    def construir_interfaz(self):
        # Arma los campos y el boton del formulario.
        contenedor = tk.Frame(self, bg="#ffffff", padx=32, pady=28)
        contenedor.place(relx=0.5, rely=0.5, anchor="center")

        logo = self.cargar_logo()
        if logo is not None:
            tk.Label(
                contenedor,
                image=logo,
                bg="#ffffff",
            ).pack(pady=(0, 12))


        titulo = tk.Label(
            contenedor,
            text="Restaurante App",
            bg="#ffffff",
            fg="#1f2a44",
            font=("Arial", 22, "bold"),
        )
        titulo.pack(pady=(0, 6))

        subtitulo = tk.Label(
            contenedor,
            text="Inicio de sesion",
            bg="#ffffff",
            fg="#516173",
            font=("Arial", 11),
        )
        subtitulo.pack(pady=(0, 22))

        tk.Label(
            contenedor,
            text="Usuario",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w")

        self.usuario_entry = tk.Entry(contenedor, width=30, font=("Arial", 11))
        self.usuario_entry.pack(pady=(4, 14), ipady=4)
        self.usuario_entry.focus()

        tk.Label(
            contenedor,
            text="Contrasena",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w")

        self.contrasena_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11),
            show="*",
        )
        self.contrasena_entry.pack(pady=(4, 14), ipady=4)
        self.contrasena_entry.bind("<Return>", lambda evento: self.iniciar_sesion())

        self.mensaje_error = tk.Label(
            contenedor,
            text="",
            bg="#ffffff",
            fg="#b42318",
            font=("Arial", 10),
        )
        self.mensaje_error.pack(pady=(0, 14))

        boton = ttk.Button(
            contenedor,
            text="Iniciar sesion",
            command=self.iniciar_sesion,
            style="Login.TButton",
        )
        boton.pack(fill="x")

    def iniciar_sesion(self):
        # Lee los datos y revisa si el usuario puede entrar.
        assert self.usuario_entry is not None
        assert self.contrasena_entry is not None
        assert self.mensaje_error is not None

        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:
            self.mensaje_error.config(text="Ingrese usuario y contrasena.")
            return

        usuario_validado = self.restaurante_servicio.validar_acceso(usuario, contrasena)

        if usuario_validado is None:
            self.mensaje_error.config(text="Credenciales incorrectas.")
            return

        self.mensaje_error.config(text="")
        self.al_inicar_sesion(usuario_validado)

