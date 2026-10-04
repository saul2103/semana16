class Producto:
    # Guarda la informacion basica de cada producto.
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    @staticmethod
    def validar_texto(valor, campo):
        # Revisa que el dato tenga algun contenido.
        if not valor or not valor.strip():
            raise ValueError(f"El campo {campo} no puede estar vacio.")

        return valor.strip()

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        # Guarda el codigo despues de revisarlo.
        self._codigo = self.validar_texto(valor, "codigo")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        # Guarda el nombre despues de revisarlo.
        self._nombre = self.validar_texto(valor, "nombre")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        # Convierte el precio y evita valores negativos.
        if isinstance(valor, str):
            valor = valor.strip().replace(",", ".")
            try:
                valor = float(valor)
            except ValueError:
                raise ValueError("El precio debe ser un número válido.")

        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El precio debe ser un número positivo.")
        self._precio = float(valor)