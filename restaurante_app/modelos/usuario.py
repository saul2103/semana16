class Usuario:
    # Guarda los datos de una persona que puede entrar al sistema.
    def __init__(self, identificador, nombre, usuario, contrasena):
        self.identificador = identificador
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena

    @staticmethod
    def validar_texto(valor, campo):
        # Revisa que el dato no quede vacio.
        if not valor or not valor.strip():
            raise ValueError(f"El campo {campo} no puede estar vacio.")

        return valor.strip()

    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def identificador(self, valor):
        # Guarda el identificador limpio.
        self._identificador = self.validar_texto(valor, "identificador")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        # Guarda el nombre limpio.
        self._nombre = self.validar_texto(valor, "nombre")

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        # Guarda el nombre de acceso.
        self._usuario = self.validar_texto(valor, "usuario")

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, valor):
        # Guarda la clave de acceso.
        self._contrasena = self.validar_texto(valor, "contrasena")