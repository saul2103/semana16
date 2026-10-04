# Restaurante App

**Estudiante:** Bryan Saul Iza Llano

Aplicacion de escritorio para administrar usuarios, productos y ventas de un restaurante. Esta desarrollada en Python con Tkinter y organiza la interfaz, los modelos, los servicios y los datos JSON en modulos separados.

## Funcionalidades

- Inicio de sesion con validacion de credenciales y roles.
- Panel principal con resumen de usuarios, productos y ventas.
- Administracion de usuarios: registrar, consultar, actualizar y eliminar. Esta seccion esta disponible para el rol administrador.
- Administracion de productos: registrar, buscar por codigo, actualizar, eliminar y limpiar el formulario.
- Registro de ventas asociadas a un usuario y un producto existentes.
- Historial de ventas con identificador, usuario, producto y fecha.
- Generacion de reportes PDF de ventas, con resumen y detalle.
- Actualizacion de tablas y totales despues de las operaciones.
- Persistencia local de usuarios, productos y ventas en archivos JSON.

## Interfaz

La ventana principal incluye un menu lateral para Inicio, Usuarios, Productos y Ventas, un area de contenido y una barra de estado. Los formularios y las tablas se organizan en paneles separados; en Usuarios, el formulario aparece a la izquierda y la tabla a la derecha.

Los botones usan iconos reutilizados por la aplicacion y el menu restablece su estado al cambiar de seccion. Esto evita que un boton parezca quedarse presionado y permite seguir navegando despues de abrir Ventas.

## Inicio de sesion

Estas cuentas estan incluidas en `restaurante_app/datos/usuarios.json`:

| Rol | Usuario | Contrasena |
| --- | --- | --- |
| Administrador | `saul` | `saul123` |
| Cocinero | `cocinero1` | `cocina123` |
| Cocinero | `cocinero2` | `cocinero1234` |

Las contrasenas se guardan como texto en el JSON local. Estas cuentas son datos de demostracion; no se recomienda usar este mecanismo para un sistema en produccion.

## Gestion de usuarios y roles

La pantalla **Usuarios** presenta el formulario a la izquierda y la tabla de cuentas a la derecha. Desde ella se puede registrar, seleccionar, actualizar, eliminar y limpiar usuarios. Al seleccionar una fila se cargan sus datos en el formulario. La contrasena se muestra enmascarada mientras se escribe.

Los roles disponibles son:

- `administrador`: puede abrir la pantalla Usuarios y administrar cuentas. No puede eliminar su propia cuenta y, al editarse a si mismo, el selector de rol queda deshabilitado.
- `cocinero`: rol disponible para las cuentas de cocina. La pantalla Usuarios comprueba que la cuenta activa sea administradora antes de mostrar la gestion.

El servicio valida que los campos requeridos no esten vacios, que el identificador no se repita, que el nombre de acceso sea unico y que el rol sea `administrador` o `cocinero`. En la interfaz actual, la comprobacion de permisos explicita se aplica a Usuarios; Productos y Ventas no realizan una comprobacion de rol equivalente.

## Eventos, `bind()` y callbacks

Tkinter ejecuta callbacks cuando ocurre una accion. En los botones, `command=` recibe la funcion que se ejecutara al hacer clic; se pasa la referencia sin parentesis para no ejecutarla durante la construccion de la interfaz:

```python
ttk.Button(contenedor, text="Iniciar sesion", command=self.iniciar_sesion)
```

`bind()` conecta un evento del teclado o de un widget a una funcion. A diferencia de `command=`, el callback de `bind()` recibe el objeto `event` como argumento. Por ejemplo, Enter en el campo de contrasena inicia sesion:

```python
self.contrasena_entry.bind("<Return>", lambda evento: self.iniciar_sesion())
```

Eventos conectados en la gestion de usuarios:

- `<<TreeviewSelect>>`: al seleccionar una fila de la tabla, carga ese usuario en el formulario.
- `<<ComboboxSelected>>`: actualiza el texto que indica el rol seleccionado.
- `<Return>` en el selector de rol: intenta registrar el usuario del formulario.
- `<Escape>` en los campos, el selector de rol y la tabla: limpia el formulario.
- Clic en un boton: su `command=` llama al callback de registrar, actualizar, eliminar o limpiar.

Los callbacks de la interfaz validan la accion, llaman a `RestauranteServicio` para aplicar la operacion y muestran mensajes de resultado o error.

## Datos locales

Los archivos de `restaurante_app/datos/` almacenan:

- `usuarios.json`: identificador, nombre, usuario, contrasena y rol.
- `productos.json`: codigo, nombre y precio.
- `ventas.json`: identificador, usuario asociado, producto asociado y fecha.

`ArchivoServicio` centraliza la lectura y escritura. Los archivos inexistentes o vacios se inicializan como listas JSON. Mantenga su contenido en formato JSON valido para evitar errores al cargar los datos.

### Persistencia de `usuarios.json`

Cada usuario se guarda como un objeto con `identificador`, `nombre`, `usuario`, `contrasena` y `rol`. Al registrar, actualizar o eliminar una cuenta, `RestauranteServicio.guardar_usuarios()` convierte la lista actual de usuarios a esos campos y `ArchivoServicio` escribe el resultado en `restaurante_app/datos/usuarios.json`. Los cambios quedan guardados inmediatamente y se conservan al cerrar la aplicacion.

Si `usuarios.json` no existe o esta vacio, el servicio inicia con las cuentas de demostracion. El archivo debe contener una lista JSON valida. Importante: las contrasenas se almacenan sin cifrar; esta persistencia es para un proyecto local de aprendizaje, no para proteger cuentas reales.

## Estructura

```text
README.md
restaurante_app/
|-- main.py
|-- assets/
|   |-- icons/
|   |-- logo/
|-- datos/
|   |-- productos.json
|   |-- usuarios.json
|   |-- ventas.json
|-- modelos/
|   |-- producto.py
|   |-- usuario.py
|   |-- venta.py
|-- servicios/
|   |-- archivo_servicio.py
|   |-- reporte_servicio.py
|   |-- restaurante_servicio.py
|-- ui/
    |-- login_view.py
    |-- main_view.py
```

## Requisitos

- Python 3.
- Tkinter disponible en la instalacion de Python.
- ReportLab, solo para generar reportes PDF.

Instale ReportLab desde la carpeta raiz del proyecto si necesita exportar reportes:

```powershell
py -m pip install reportlab
```

Sin ReportLab, se pueden utilizar las demas funciones de la aplicacion; la opcion de reporte indicara que falta esa dependencia.

## Ejecucion de `main.py`

1. Instale Python 3 y compruebe que Tkinter este disponible. En Windows puede probarlo con `py -m tkinter`; debe abrirse una ventana de demostracion.
2. Abra en VS Code la carpeta raiz del proyecto, la que contiene este README y la carpeta `restaurante_app`.
3. Abra una terminal integrada y confirme que la ruta actual sea esa carpeta raiz.
4. Inicie la aplicacion con:

```powershell
py restaurante_app\main.py
```

Tambien puede entrar primero en `restaurante_app` y ejecutar el archivo desde ahi:

```powershell
cd restaurante_app
py main.py
```

En Linux o macOS, desde la carpeta raiz:

```bash
python3 restaurante_app/main.py
```

`main.py` crea la ventana Tkinter, carga los datos desde `datos/`, prepara los servicios y muestra el login. Inicie sesion con una de las cuentas de demostracion de la tabla anterior. ReportLab solo es necesario para generar reportes PDF; el resto de la aplicacion puede ejecutarse sin ese paquete.

## Verificacion

Para comprobar la sintaxis de los modulos:

```powershell
py -m compileall -q restaurante_app
```
