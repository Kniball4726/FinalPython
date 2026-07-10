import time
from colorama import Fore, Style
from src.helpers.helper import borrar_pantalla as borrarPantalla, salir_aplicacion
from src.pedidos.pedidos import agregarPedido, buscarPedido, verPedidos, modificarPedido, eliminarPedido
from src.usuarios.usuarios import subMenu
from src.sedes.sedes import sedes, sedeP


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


pedidos = {
    23456: {
            "cliente": "Ruben blale",
            "bultos": 3,
            "logistica": "Transporte Sur",
            "operario": "Juan Pérez",
            "productos": [
                {"producto": "Whey protein 2lbs chocolate", "cantidad": 10},
                {"producto": "Creatine 500 gr", "cantidad": 20}
            ]
        }
    }


def ingreso():
    """
    Función que maneja el proceso de ingreso al sistema. Solicita al usuario que ingrese su DNI, nombre de usuario y contraseña. Verifica si el DNI está registrado en el sistema y si las credenciales son correctas. Si el ingreso es exitoso, redirige al menú principal según el rol del usuario (Admin o Usuario). Si el ingreso falla, muestra mensajes de error y vuelve a solicitar los datos de ingreso.
     - Si el DNI no está registrado, muestra un mensaje indicando que el DNI no se encuentra registrado y vuelve a solicitar los datos de ingreso.
     - Si el usuario o la contraseña son incorrectos, muestra un mensaje indicando que el usuario o la contraseña son incorrectos y vuelve a solicitar los datos de ingreso.
     - Si el usuario interrumpe el proceso de ingreso (por ejemplo, presionando CtrlC), muestra un mensaje indicando que se está saliendo del sistema y termina la ejecución del programa.
     - Si el usuario ingresa un valor no numérico para el DNI, muestra un mensaje indicando que se debe indicar un número válido y vuelve a solicitar los datos de ingreso.
     - Si el usuario ingresa un valor no numérico para el DNI, muestra un mensaje indicando que se debe indicar un número válido y vuelve a solicitar los datos de ingreso.  
    """
   
    global dni, password, user, usuarios
   
    try:
        while True:
            borrarPantalla()
            print(Fore.GREEN + Style.BRIGHT + "Bienvenido al sistema de pedidos mayoristas.\nDebe indicar sus datos para ingresar\n\n" + Style.RESET_ALL)
            print(Fore.RED + "Para salir coloque DNI 1" + Style.RESET_ALL)
            dni=int(input("\nIndique su DNI: "))
           
            if dni in usuarios:
                user=input("Indique su usuario: ").capitalize()
                password=input("Indique su contraseña: ")

                if user == usuarios[dni]["user"] and usuarios[dni]["password"] == password:
                    role = usuarios[dni]["role"]
                    while True:
                        print(f"{'='*50}\nSedes disponibles:\n{'='*50}")
                        for i, sede in enumerate(sedeP, start=1):
                            print(f"{i}. {sede}")
                    
                            opcion_sede = int(input("\nIndique el número de la sede a la que pertenece: "))
                            if 1 <= opcion_sede <= len(sedeP):
                                sede = sedeP[opcion_sede - 1]
                                menuPrincipal(role, user, sede)
                                break
                            else:
                                input("\nNúmero de sede inválido. Presione Enter para continuar...")
                                continue
                    
                elif user != usuarios[dni]["user"] and usuarios[dni]["password"] == password:
                    print(Fore.RED + Style.BRIGHT+"\nUsuario incorrecto" + Style.RESET_ALL )
                    time.sleep(1)
                    continue
                elif user == usuarios[dni]["user"] and usuarios[dni]["password"] != password:
                    print(Fore.RED + Style.BRIGHT+"\nContraseña incorrecta" + Style.RESET_ALL)
                    time.sleep(1)   
                    continue
                else:
                    print(Fore.RED + Style.BRIGHT +"\nUsuario y contraseña incorrecto"+Style.RESET_ALL)
                    time.sleep(1)
                    continue
            elif dni == 1:
                print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ."+ Style.RESET_ALL)
                time.sleep(1)
                salir_aplicacion()
            else:
                print(Fore.RED+Style.BRIGHT+"\nEl DNI no se encuentra registrado"+Style.RESET_ALL)
                time.sleep(1)   
                continue

    except ValueError:
        print(Fore.RED + Style.BRIGHT + "\nIndique un número valido" + Style.RESET_ALL)
        time.sleep(1)
        ingreso()
    except TypeError:
        print(Fore.RED + Style.BRIGHT + "\nIndique un número valido" + Style.RESET_ALL)
        time.sleep(1)
        ingreso()

def menuPrincipal(role, user, sede):
    """Función que muestra el menú principal del sistema. Permite a los usuarios seleccionar diferentes opciones para gestionar pedidos y usuarios, dependiendo de su rol (Admin o Usuario). Redirige a las funciones correspondientes según la opción seleccionada por el usuario.
     - Opción 1: Agregar pedido. Redirige a la función 'agregarPedido' para agregar un nuevo pedido al sistema.
     - Opción 2: Buscar pedido. Redirige a la función 'buscarPedido' para buscar un pedido existente en el sistema.
     - Opción 3: Ver pedidos. Redirige a la función 'verPedidos' para mostrar la lista de pedidos registrados en el sistema.
     - Opción 4: Modificar pedido. Redirige a la función 'modificarPedido' para modificar los datos de un pedido existente en el sistema.
     - Opción 5: Eliminar pedido. Redirige a la función 'eliminarPedido' para eliminar un pedido existente en el sistema.
     - Opción 6: Gestión de usuarios (solo para Admin). Redirige a la función 'subMenu' para mostrar el submenú de gestión de usuarios.
     - Opción 7: Salir. Redirige a la función 'ingreso' para volver al proceso de ingreso al sistema.
     - Opción no válida: Si el usuario selecciona una opción que no está en el menú, muestra un mensaje indicando que la opción no es válida y vuelve a mostrar el menú principal."""

    global opcion
    try:
        while opcion != "0":
            borrarPantalla()
            menu=[f"\n{'='*50}{Fore.GREEN}{Style.BRIGHT}\nBienvenid@s al menú principal{Style.RESET_ALL}\n{Style.BRIGHT}{'='*50}\nUsuario:{Style.RESET_ALL}{user}\n{Style.BRIGHT}Rol:{Style.RESET_ALL}{role}\n{Style.BRIGHT}Sede:{Style.RESET_ALL}{sede}\n{'='*50}{Style.RESET_ALL}","1.-Agregar pedido","2.-Buscar pedido","3.-Ver pedidos","4.-Modificar pedido","5.-Eliminar pedido"]
            # Agregar opciones adicionales de forma segura
            if role == "Admin":
                menu.append("6.-Gestión de usuarios")
                menu.append("7.-Gestión de sedes")
                menu.append("8.-Cambiar usuario")
                menu.append("0.-Salir")
            else:
                menu.append("8.-Cambiar usuario")
                menu.append("0.-Salir")

            for m in menu:
                print(m)

            opcion=input("\nIndique opción: ").strip()

            match opcion:
                case "1":
                    agregarPedido(sede)
                case "2":
                    buscarPedido(sede)
                case "3":
                    verPedidos(sede)
                case "4":
                    modificarPedido(sede)
                case "5":
                    eliminarPedido(sede)
                case "6":
                    if role == "Admin":
                        subMenu(dni)
                    else:
                        print("\nOpción no válida")
                        time.sleep(1)   
                        continue
                case "7":
                    if role == "Admin":
                        sedes()
                    else:
                        print("\nOpción no válida")
                        time.sleep(1)
                        continue
                case "8":
                    ingreso()
                case "0":
                    print("\nSaliendo . . .")
                    time.sleep(1)
                    salir_aplicacion()
                case _:
                    print("\nOpción no válida")
                    time.sleep(1)
                    continue
    except ValueError:
        print("\nOpción no válida, debe indicar un número")
        time.sleep(1)
        menuPrincipal(role, user, sede)
    except KeyboardInterrupt:
        print("\nSaliendo . . .")
        time.sleep(1)
        salir_aplicacion()
    except TypeError:
        print("\nOpción no válida, debe indicar un número")
        time.sleep(1)
        menuPrincipal(role, user, sede)
    except Exception as e:
        print(f"\nOcurrió un error: {e}" )
        time.sleep(1)
        menuPrincipal(role, user, sede)

    return opcion, role, user, sede

