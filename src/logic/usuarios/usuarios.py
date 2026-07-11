import time
from colorama import Fore, Style
from src.helpers.helper import borrar_pantalla as borrarPantalla, salir_aplicacion

menu:list=[]
opcion:str=""
dni:int=0
user:str=""
password:str=""
usuarios:dict={}
submenu:list=[]

usuarios={
    95777596:{
        "user":"Gregory",
        "password":"admin123",
        "role":"Admin"
    },
    12345678:{
        "user":"Usuario",
        "password":"usuario123",
        "role":"User"
    }
}

def agregarUsuario():
    """Función que permite agregar un nuevo usuario al sistema."""
   
    dni:int=0
    user:str=""
    password:str=""
    role:str=""
    global usuarios
   
    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{'='*50}\nAgregar nuevo usuario\n{'='*50}" + Style.RESET_ALL)
       
        dni=int(input("\nIndique DNI: "))
       
        if dni in usuarios:
            input(Fore.RED + Style.BRIGHT + "\nEl DNI ya está registrado" + Style.RESET_ALL)
            return
        else:
            user=input("Indique usuario: ").capitalize()
            password=input("Indique contraseña: ")

            if not user or not password:
                input(Fore.RED + Style.BRIGHT + "\nUsuario y contraseña no pueden estar vacíos" + Style.RESET_ALL)
                subMenu()

            print(Fore.GREEN + Style.BRIGHT + f"{'='*50}" + Style.RESET_ALL)
            print("Roles disponibles: Admin, User")
            print(f"{'='*50}")  
            role=input("Indique rol (Admin/User): ").capitalize()
       
            if role != "Admin" and role != "User":
                input(Fore.RED + Style.BRIGHT + "\nRol no válido, se asignará el rol de Usuario por defecto" + Style.RESET_ALL)
                role = "User"
       
        usuarios[dni] = {
            "user": user,
            "password": password,
            "role": role
        }
       
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"\n{'='*50}" + Style.RESET_ALL)
        print(Fore.GREEN + Style.BRIGHT + f"✓ Usuario registrado exitosamente" + Style.RESET_ALL)
        print(Fore.GREEN + Style.BRIGHT + f"{'='*50}" + Style.RESET_ALL)
        print(f"DNI: {dni}")
        print(f"Usuario: {user}")
        print(f"Rol: {role}")
        input("\nPresione Enter para continuar..." )
       
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido para el DNI" + Style.RESET_ALL)
        subMenu()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(1)
        salir_aplicacion()
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido para el DNI" + Style.RESET_ALL)
        subMenu()
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}" + Style.RESET_ALL)


def buscarUsuario():
    """Función que busca un usuario por DNI y muestra sus datos."""
    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{'='*50}\nBuscar Usuario\n{'='*50}" + Style.RESET_ALL)
       
        dni = int(input("\nIndique DNI a buscar: "))
       
        if dni in usuarios:
            borrarPantalla()
            
            print(Fore.GREEN + Style.BRIGHT + f"✓ Usuario Encontrado" + Style.RESET_ALL)
            print(Fore.GREEN + Style.BRIGHT + f"\n{'='*50}" + Style.RESET_ALL)
            print(Fore.GREEN + Style.BRIGHT + f"Datos del Usuario:" + Style.RESET_ALL)
            print(Fore.GREEN + Style.BRIGHT + f"{'='*50}" + Style.RESET_ALL)
            print(f"DNI: {dni}")
            print(f"Usuario: {usuarios[dni]['user']}")
            print(f"Contraseña: {usuarios[dni]['password']}")
            print(f"Rol: {usuarios[dni]['role']}")
            input(Fore.GREEN + Style.BRIGHT + "\nPresione Enter para continuar..." + Style.RESET_ALL)
        else:
            input(Fore.RED + Style.BRIGHT + "\n✗ Usuario no encontrado" + Style.RESET_ALL)
           
       
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido para el DNI" + Style.RESET_ALL)
        subMenu()
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido para el DNI" + Style.RESET_ALL)
        subMenu()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(1)
        salir_aplicacion()
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}" + Style.RESET_ALL)
        subMenu()
        
def verUsuarios():
    """Función que muestra la lista de usuarios registrados en el sistema."""
   
    borrarPantalla()
    print(Fore.GREEN + Style.BRIGHT + f"{'='*50}\nLista de usuarios registrados\n{'='*50}" + Style.RESET_ALL)
   
    if not usuarios:
        input(Fore.RED + Style.BRIGHT + "\nNo hay usuarios registrados." + Style.RESET_ALL)
    else:
        for dni, datos in usuarios.items():
            print(f"\nDNI: {dni}")
            print(f"Usuario: {datos['user']}")
            print(f"Rol: {datos['role']}")
            print(f"{'─'*66}")
   
    input(Fore.GREEN + Style.BRIGHT + "\nPresione Enter para volver al submenú" + Style.RESET_ALL)

def modificarUsuario():
    """Función que permite modificar los datos de un usuario existente."""
    global usuarios
   
    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{'='*50}\nModificar Usuario\n{'='*50}" + Style.RESET_ALL)
       
        dni = int(input("\nIndique DNI del usuario a modificar: "))
       
        if dni in usuarios:
            print(Fore.GREEN + Style.BRIGHT + f"{'='*50}" + Style.RESET_ALL)
            print(Fore.GREEN + Style.BRIGHT + f"Usuario Encontrado - DNI {dni}" + Style.RESET_ALL)
            print(Fore.GREEN + Style.BRIGHT + f"{'='*50}" + Style.RESET_ALL)
            print(f"Usuario actual: {usuarios[dni]['user']}")
            print(f"Rol actual: {usuarios[dni]['role']}")
           
            print("\n¿Qué desea modificar?")
            print("1. Usuario")
            print("2. Contraseña")
            print("3. Rol")
            print("0. Cancelar")
           
            opcion = input("\nSeleccione opción: ").strip()
            match opcion:
                case "1":
                   nuevo_user = input("Nuevo usuario: ").capitalize()
                   usuarios[dni]['user'] = nuevo_user
                   input(Fore.GREEN + Style.BRIGHT + "\nUsuario modificado exitosamente" + Style.RESET_ALL)
               
                case "2":
                    nueva_password = input("Nueva contraseña: ")
                    usuarios[dni]['password'] = nueva_password
                    input(Fore.GREEN + Style.BRIGHT + "\nContraseña modificada exitosamente" + Style.RESET_ALL)
               
                case "3":
                    print("Roles disponibles: Admin, User")
                    nuevo_role = input("Nuevo rol (Admin/User): ").capitalize()
                    if nuevo_role not in ["Admin", "User"]:
                        input(Fore.RED + Style.BRIGHT + "\nRol no válido" + Style.RESET_ALL)
                        modificarUsuario()
                    usuarios[dni]['role'] = nuevo_role
                    input(Fore.GREEN + Style.BRIGHT + "\nRol modificado exitosamente" + Style.RESET_ALL)
               
                case "0":
                    input(Fore.RED + Style.BRIGHT + "\nOperación cancelada" + Style.RESET_ALL)
                    modificarUsuario()
                case _:
                    input(Fore.RED + Style.BRIGHT + "\nOpción no válida" + Style.RESET_ALL)
                    modificarUsuario()
               
        else:
            input(Fore.RED + Style.BRIGHT + "\nDNI no registrado" + Style.RESET_ALL)
            modificarUsuario()
   
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido para el DNI" + Style.RESET_ALL)
        subMenu()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(1)
        salir_aplicacion()
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido para el DNI" + Style.RESET_ALL)
        subMenu()
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}" + Style.RESET_ALL)
        subMenu()
   
def eliminarUsuario():
    """Función que permite eliminar un usuario registrado en el sistema."""
    global usuarios
   
    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{'='*50}\nEliminar Usuario\n{'='*50}" + Style.RESET_ALL)
       
        dni = int(input("\nIndique DNI del usuario a eliminar: "))
       
        if dni in usuarios:
            print(f"{'='*50}")
            print(f"Usuario a Eliminar - DNI {dni}")
            print(f"{'='*50}")
            print(f"Usuario: {usuarios[dni]['user']}")
            print(f"Rol: {usuarios[dni]['role']}")
           
            confirmacion = input("¿Está seguro? Escriba 'S' para confirmar: ").strip().upper()
           
            if confirmacion == "S":
                del usuarios[dni]
                input(Fore.GREEN + Style.BRIGHT + f"\n✓ Usuario con DNI {dni} eliminado exitosamente" + Style.RESET_ALL)
            else:
                input(Fore.RED + Style.BRIGHT + "\nOperación cancelada" + Style.RESET_ALL)
        else:
            input(Fore.RED + Style.BRIGHT + "\nDNI no registrado" + Style.RESET_ALL)

    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido para el DNI" + Style.RESET_ALL)
        subMenu()
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido para el DNI" + Style.RESET_ALL)
        subMenu()
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}" + Style.RESET_ALL)
        subMenu()

def subMenu(dni:int=0):
    """
    Función que muestra el submenú de gestión de usuarios para los administradores. Permite agregar, buscar, ver, modificar y eliminar usuarios, así como volver al menú principal. Redirige a las funciones correspondientes según la opción seleccionada por el usuario.
     - Opción 1: Agregar usuario. Redirige a la función 'agregarUsuario' para agregar un nuevo usuario al sistema.
     - Opción 2: Buscar usuario. Redirige a la función 'buscarUsuario' para buscar un usuario existente en el sistema.
     - Opción 3: Ver usuarios. Redirige a la función 'verUsuarios' para mostrar la lista de usuarios registrados en el sistema.
     - Opción 4: Modificar usuario. Redirige a la función 'modificarUsuario' para modificar los datos de un usuario existente en el sistema.
     - Opción 5: Eliminar usuario. Redirige a la función 'eliminarUsuario' para eliminar un usuario existente en el sistema.
     - Opción 6: Volver al menú principal. Redirige a la función 'menuPrincipal' para volver al menú principal del sistema.
     - Opción no válida: Si el usuario selecciona una opción que no está en el submenú, muestra un mensaje indicando que la opción no es válida y vuelve a mostrar el submenú.
    """
    global opcion,submenu
    opcion = ""  # Resetear para que el while funcione correctamente
    try:
        while opcion != "0":
            borrarPantalla()
            print(Fore.GREEN + Style.BRIGHT + f"{'='*50}\nMenú gestión de usuarios\n{'='*50}" + Style.RESET_ALL)

            submenu=["1.-Agregar usuario","2.-Buscar usuario","3.-Ver usuarios","4.-Modificar usuario","5.-Eliminar usuario","0.-Volver al menú principal"]
            for s in submenu:
                print(s)

            opcion=input("\nIndique opción: ").strip()

            match opcion:
                case "1":
                    agregarUsuario()
                case "2":
                    buscarUsuario()
                case "3":
                    verUsuarios()
                case "4":
                    modificarUsuario()
                case "5":
                    eliminarUsuario()
                case "0":
                    input(Fore.GREEN + Style.BRIGHT + "\nVolviendo al menú principal . . ." + Style.RESET_ALL)
                    continue
                case _:
                    input(Fore.RED + Style.BRIGHT + "\nOpción no válida" + Style.RESET_ALL)
                    continue
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        subMenu()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(2)
        salir_aplicacion()
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        subMenu()
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}" + Style.RESET_ALL)
        subMenu()
