import builtins
import os


def borrar_pantalla():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def salir_aplicacion():
    """Cierra la aplicación de manera consistente en consola y en ejecutables."""
    raise SystemExit(0)


builtins.exit = salir_aplicacion