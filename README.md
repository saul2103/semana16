# Restaurante App

**Estudiante:** Bryan Saul Iza Llano

Aplicacion de escritorio para gestionar un restaurante con Python y Tkinter. El proyecto sigue una separacion clara entre interfaz, modelo de datos, servicios y persistencia local en archivos JSON. Ademas, incorpora la funcionalidad de ventas para registrar operaciones del negocio y mantener un historial actualizado.

## Objetivo del proyecto

La aplicacion permite iniciar sesion, consultar usuarios, administrar productos y registrar ventas de manera sencilla desde una interfaz grafica. Todo el flujo se maneja localmente sin dependencia de una base de datos externa, usando archivos JSON como almacenamiento principal.

## Funcionalidades principales

- Inicio de sesion con validacion de usuario y contrasena.
- Vista principal con menu lateral para navegar entre secciones.
- Registro, consulta, actualizacion y eliminacion de productos.
- Registro de ventas con seleccion de usuario y producto.
- Visualizacion de ventas registradas en una tabla con columnas y scroll.
- Persistencia local en archivos JSON para usuarios, productos y ventas.
- Barra de estado con conteo de usuarios, productos y ventas.
- Interfaz visual con estilos, colores, iconos y mejor distribucion de elementos.
- Validaciones para evitar campos vacios, codigos duplicados y datos invalidos.
- Mensajes informativos para exito y errores.

## Mejoras implementadas en la interfaz

Se han incorporado mejoras visuales y funcionales para que la aplicacion sea mas clara y usable:

- Menu lateral con distintas opciones: Inicio, Usuarios, Productos y Ventas.
- Estructura principal con contenedor central y barra inferior de estado.
- Estilos personalizados para botones y tablas.
- Uso de iconos para acciones principales como registrar, buscar, eliminar y cerrar sesion.
- Mejor organizacion de formularios y listados mediante frames y grids.
- Ajuste del ancho de tablas y paneles para que el contenido se adapte mejor a la ventana actual.
- La seccion Ventas presenta un formulario de seleccion y una tabla con historial de ventas.
- Los listados de productos, usuarios y ventas se actualizan automaticamente tras cada operacion.

## Modulo de ventas

La funcionalidad de ventas es una de las mejoras mas relevantes del proyecto. En la vista de ventas se puede:

1. Seleccionar un usuario y un producto desde combobox.
2. Registrar una venta con la fecha actual.
3. Guardar la operacion automaticamente en el archivo JSON de ventas.
4. Ver el historial de ventas en una tabla organizada.
5. Revisar los datos relacionados con cada venta en una sola vista.

Cada venta queda asociada a:

- identificador de la venta
- usuario responsable
- producto vendido
- fecha en la que se registro

Esto permite llevar un control basico del negocio desde la aplicacion.

## Persistencia de datos

La aplicacion usa archivos JSON locales para conservar la informacion del restaurante:

- `restaurante_app/datos/usuarios.json`: guarda identificadores, nombre, usuario y contrasena.
- `restaurante_app/datos/productos.json`: guarda codigo, nombre y precio.
- `restaurante_app/datos/ventas.json`: guarda cada venta con su identificador, usuario, producto y fecha.

La clase `ArchivoServicio` se encarga de leer y escribir los archivos, creando listas vacias si no existen o si el contenido no es valido. De esta manera, las operaciones sobre usuarios, productos y ventas se vuelven persistentes y visibles cada vez que se reinicia la aplicacion.

## Logica de negocio

El servicio principal `RestauranteServicio` centraliza la mayor parte de la logica del sistema. Entre sus funciones se encuentran:

- validacion de acceso
- conteo de usuarios, productos y ventas
- listado de registros
- busqueda de producto por codigo
- registro, actualizacion y eliminacion de productos
- registro de ventas con validacion de usuario y producto existentes
- generacion de identificadores para ventas
- guardado automatico en JSON

Esto permite mantener un codigo ordenado y facilitar las futuras ampliaciones.

## Estructura del proyecto

```text
SEMANA 15/
|-- README.md
|-- restaurante_app/
    |-- main.py
    |-- datos/
    |   |-- productos.json
    |   |-- usuarios.json
    |   |-- ventas.json
    |-- modelos/
    |   |-- producto.py
    |   |-- usuario.py
    |   |-- venta.py
    |   |-- __init__.py
    |-- servicios/
    |   |-- archivo_servicio.py
    |   |-- restaurante_servicio.py
    |   |-- __init__.py
    |-- ui/
    |   |-- login_view.py
    |   |-- main_view.py
    |   |-- __init__.py
    |-- assets/
        |-- icons/
        |-- logo/
```

## Componentes y tecnologias usadas

La interfaz se desarrollo con Tkinter, un conjunto de widgets de Python para crear aplicaciones de escritorio:

- `Tk`: ventana principal.
- `Frame`: separacion de secciones.
- `Label`: textos, titulos y mensajes.
- `Entry`: campos para usuario, contrasena, codigo y nombre.
- `LabelFrame`: agrupacion de formularios y listados.
- `ttk.Button`: botones visuales con estilo moderno.
- `ttk.Combobox`: seleccion de usuario y producto en ventas.
- `ttk.Treeview`: tablas para usuarios, productos y ventas.
- `ttk.Scrollbar`: desplazamiento vertical de tablas.
- `PhotoImage`: carga de logo e iconos.
- `messagebox`: avisos de exito o validacion.

## Pantallas principales

### Inicio de sesion

La primera vista permite iniciar sesion con usuario y contrasena. Si los datos son correctos se accede a la interfaz principal. Cuando no son validos, se muestra un mensaje de error.

Usuario de prueba incluido:

```text
Usuario: saul
Contrasena: saul123
```

### Vista principal

La pantalla principal contiene un menu lateral y un area de contenido. Desde alli se puede acceder a:

- Inicio
- Usuarios
- Productos
- Ventas

### Seccion de ventas

En la seccion de ventas se presentan dos elementos principales:

- formulario de registro con dos combobox para seleccionar usuario y producto
- tabla de ventas registradas con la informacion completa

Esta vista ofrece una experiencia mas completa para trabajar con el historial de ventas del restaurante.

## Operaciones sobre productos

La seccion Productos permite realizar lo siguiente:

1. Registrar un producto nuevo.
2. Buscarlo por codigo.
3. Actualizar sus datos.
4. Eliminarlo del registro.
5. Limpiar el formulario.

El sistema valida que el codigo no se repita, que los textos no queden vacios y que el precio sea numerico y positivo.

## Operaciones sobre ventas

La seccion Ventas permite:

1. Seleccionar un usuario.
2. Seleccionar un producto.
3. Registrar la venta.
4. Guardarla automaticamente.
5. Mostrar el historial actualizado en la tabla.

## Requisitos

- Python 3 instalado.
- Tkinter disponible en el entorno.
- Archivos del proyecto conservados en la estructura original.

No se requieren paquetes externos adicionales.

## Como ejecutar el proyecto

1. Abrir una terminal.
2. Ubicarse en la carpeta raiz del proyecto.
3. Ejecutar:

```powershell
py restaurante_app\main.py
```

O en Linux o macOS:

```bash
python restaurante_app/main.py
```

## Verificacion de codigo

Se puede comprobar la integridad del proyecto con:

```powershell
py -m compileall -q restaurante_app
```

## Notas finales

El proyecto combina una interfaz grafica funcional con un modelo de persistencia simple basado en JSON. Gracias a esta estructura, es facil mantener los datos, ampliar la app con nuevas funciones y visualizar operaciones del negocio como ventas, usuarios y productos desde una sola aplicacion.
