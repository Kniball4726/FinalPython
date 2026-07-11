# FinalPython

Aplicación de consola en Python para la gestión de pedidos mayoristas, sedes y usuarios.

## Descripción

Este proyecto es un sistema de pedidos en modo texto que permite:

- Iniciar sesión con DNI, usuario y contraseña.
- Gestionar pedidos por sede.
- Agregar, buscar, ver, modificar y eliminar pedidos.
- Administrar usuarios (solo para rol Admin): crear, buscar, listar, modificar y eliminar usuarios.
- Administrar sedes (solo para rol Admin): agregar, buscar, listar, modificar y eliminar sedes.

## Estructura del proyecto

- `init.py`: punto de entrada principal del proyecto.
- `requirements.txt`: dependencias necesarias para ejecutar el proyecto.
- `src/`: código fuente principal.
  - `helpers/helper.py`: utilidades compartidas como limpiar pantalla y salir de la aplicación.
  - `logic/ingreso/ingreso.py`: manejo de login, selección de sede y menú principal.
  - `logic/pedidos/pedidos.py`: gestión de pedidos.
  - `logic/sedes/sedes.py`: gestión de sedes.
  - `logic/usuarios/usuarios.py`: gestión de usuarios.

## Dependencias

El proyecto utiliza las siguientes dependencias principales:

- `colorama` para colorear la salida en consola.
- `pyinstaller` y herramientas relacionadas para generar ejecutables si se desea empaquetar la app.

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

### Usar un entorno virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Ejecución

Para ejecutar la aplicación desde la raíz del proyecto:

```bash
python init.py
```

## Uso

1. Ingrese un DNI registrado.
2. Ingrese el usuario y la contraseña correspondientes.
3. Seleccione la sede a la que pertenece.
4. Navegue entre las opciones del menú principal.

### Credenciales de ejemplo

- Admin:
  - DNI: `95777596`
  - Usuario: `Gregory`
  - Contraseña: `admin123`

- Usuario:
  - DNI: `12345678`
  - Usuario: `Usuario`
  - Contraseña: `usuario123`

## Funcionalidades principales

- Control de acceso con roles `Admin` y `User`.
- Gestión de pedidos asociados a sedes.
- Menú de administración de usuarios para el rol `Admin`.
- Menú de administración de sedes para el rol `Admin`.

## Notas

- El proyecto funciona como aplicación de consola y utiliza entrada estándar (`input`) para interacción.
- Las estructuras de datos actuales se almacenan en memoria mientras la aplicación está en ejecución.
- Para empaquetar el proyecto como ejecutable puede usarse `pyinstaller` con `init.py`.

## Empaquetado con PyInstaller

Si deseas distribuir la aplicación como ejecutable, instala `pyinstaller` y ejecuta:

```bash
pyinstaller --onefile init.py
```

El ejecutable resultante se generará en la carpeta `dist/`.

## Contribución

Si quieres contribuir al proyecto:

1. Haz un fork del repositorio.
2. Crea una rama nueva: `git checkout -b mejora-descripcion`.
3. Realiza los cambios y prueba la aplicación.
4. Envía un pull request con una descripción clara de la mejora.

Buenas ideas para contribuir:

- Mejorar validaciones de entrada.
- Añadir persistencia en archivos o base de datos.
- Manejar mejor los mensajes de error.
- Agregar pruebas unitarias.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.

Consulta el archivo `LICENSE` para más detalles.
