from src.pedidos.pedidos import borrarPantalla
from src.helpers.helper import salir_aplicacion
import time
from colorama import Fore, Style
sedeP:list=["Pasteur", "Av. santa fe", "Av. Cordoba", "Av. Cabildo", "Florida", "Unicenter"]
opcion:str=""



def sedes():
    """Función que muestra el menú de sedes y permite al usuario seleccionar una opción para agregar, buscar, ver, modificar o eliminar sedes. Maneja excepciones para entradas inválidas y permite al usuario volver a intentar el proceso o salir del proceso.
    - Opción 1: Agregar sede. Redirige a la función 'agregarSede' para agregar una nueva sede al sistema.
    - Opción 2: Buscar sede. Redirige a la función 'buscarSede' para buscar una sede existente en el sistema.
    - Opción 3: Ver sedes. Redirige a la función 'verSedes' para mostrar la lista de sedes registradas en el sistema.
    - Opción 4: Modificar sede. Redirige a la función 'modificarSede' para modificar los datos de una sede existente en el sistema.
    - Opción 5: Eliminar sede. Redirige a la función 'eliminarSede' para eliminar una sede existente en el sistema.
    - Opción 0: Volver al menú principal. Permite al usuario regresar al menú principal del sistema.
    - Opción no válida: Si el usuario selecciona una opción que no está en el menú, muestra un mensaje indicando que la opción no es válida y vuelve a mostrar el menú de sedes."""
    try:
        while True:
            borrarPantalla()

            sede=[f"{Fore.GREEN}{Style.BRIGHT}\n{'='*50}\nMenú sedes\n{'='*50}{Style.RESET_ALL}","1.-Agregar sede","2.-Buscar sede","3.-Ver sedes","4.-Modificar sede","5.-Eliminar sede","0.-Volver al menú principal"]
            
            for s in sede:
                print(s)
            
            opcion = input("\nSeleccione una opción: ").strip()

            match opcion:
                case "1":
                    agregarSede()
                case "2":
                    buscarSede()
                case "3":
                    verSedes()
                case "4":
                    modificarSede()
                case "5":
                    eliminarSede()
                case "0":
                    break
                case _:
                    input("\nOpción inválida. Por favor, seleccione una opción válida.")
    except ValueError:
        input("\nOpción no válida, debe indicar un número")
        sedes()
    except KeyboardInterrupt:
        print("\nSaliendo . . .")
        time.sleep(1)
        salir_aplicacion()
    except TypeError:
        input("\nOpción no válida, debe indicar un número")
        sedes()
    except Exception as e:
        input(f"\nOcurrió un error: {e}")
        sedes()
        
def agregarSede():
    """Función que permite agregar una nueva sede al sistema. Solicita al usuario que ingrese el nombre de la nueva sede y verifica si ya existe en la lista de sedes. Si la sede no existe, se agrega a la lista y se muestra un mensaje de éxito. Si la sede ya existe o el nombre ingresado está vacío, se muestra un mensaje correspondiente y se permite al usuario volver a intentar el proceso. Maneja excepciones para entradas inválidas y permite al usuario volver a intentar el proceso o salir del proceso."""
    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{ '='*50 }\nAgregar nueva sede\n{ '='*50 }" + Style.RESET_ALL)
        nsede=input("\nIndique el nombre de la nueva sede a agregar:").strip().capitalize()
        if nsede in sedeP:
            input(Fore.RED + Style.BRIGHT + "\nLa sede ya existe. Presione Enter para continuar..." + Style.RESET_ALL)
            time.sleep(1)
            return
        elif not nsede:
            input(Fore.RED + Style.BRIGHT + "\nEl nombre de la sede no puede estar vacío. Presione Enter para continuar..." + Style.RESET_ALL)
            return
        else:
            sedeP.append(nsede)
            input(Fore.GREEN + Style.BRIGHT + "\nSede agregada con éxito. Presione Enter para continuar... " + Style.RESET_ALL)
            sedes()  # Volver al menú de sedes después de agregar
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        agregarSede()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(1)
        salir_aplicacion()
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        agregarSede()
    except Exception as e:
        input(f"\nOcurrió un error: {e}")
        agregarSede()



def buscarSede():
    """Función que permite buscar una sede existente en el sistema. Solicita al usuario que ingrese el nombre de la sede a buscar y verifica si existe en la lista de sedes. Si la sede se encuentra, muestra un mensaje indicando que la sede existe; de lo contrario, muestra un mensaje indicando que la sede no se encuentra en el sistema. Maneja excepciones para entradas inválidas y permite al usuario volver a intentar el proceso o salir del proceso."""
    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{ '='*50 }\nBuscar sede\n{ '='*50 }" + Style.RESET_ALL)
        bsede=input("\nIndique el nombre de la sede a buscar: ").strip().capitalize()
        if bsede in sedeP:
            input(Fore.GREEN + Style.BRIGHT + f"\nLa sede '{bsede}' existe en el sistema. Presione Enter para continuar..." + Style.RESET_ALL)
        else:
            input(Fore.RED + Style.BRIGHT + f"\nLa sede '{bsede}' no se encuentra en el sistema. Presione Enter para continuar..." + Style.RESET_ALL    )
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        buscarSede()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(2)
        salir_aplicacion()
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        time.sleep(1)
        buscarSede()
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}" + Style.RESET_ALL)
        buscarSede()
    

def verSedes():
    """Función que muestra la lista de sedes registradas en el sistema. Muestra un encabezado con el título 'Lista de sedes' y luego enumera cada sede disponible en la lista de sedes. Permite al usuario presionar Enter para continuar después de visualizar la lista. Maneja excepciones para entradas inválidas y permite al usuario volver a intentar el proceso o salir del proceso."""
    global sedeP
    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{ '='*50 }\nLista de sedes\n{ '='*50 }" + Style.RESET_ALL)
        
        for i, sede in enumerate(sedeP, start=1):
            print(f"{i}. {sede}")

        input(Fore.GREEN + Style.BRIGHT + "\nPresione Enter para continuar..." + Style.RESET_ALL)
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        verSedes()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(1)
        salir_aplicacion()
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        verSedes()
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}" + Style.RESET_ALL)
        verSedes()
    borrarPantalla()
    print(Fore.GREEN + Style.BRIGHT + f"{ '='*50 }\nLista de sedes\n{ '='*50 }" + Style.RESET_ALL)
    

def modificarSede():
    """Función que permite modificar el nombre de una sede existente en el sistema. Solicita al usuario que ingrese el nombre de la sede a modificar y verifica si existe en la lista de sedes. Si la sede se encuentra, solicita al usuario que ingrese el nuevo nombre de la sede y verifica si ya existe en la lista de sedes. Si el nuevo nombre no existe y no está vacío, se actualiza el nombre de la sede en la lista y se muestra un mensaje
    de éxito. Si la sede no se encuentra, el nuevo nombre ya existe o está vacío, se muestra un mensaje correspondiente y se permite al usuario volver a intentar el proceso. Maneja excepciones para entradas inválidas y permite al usuario volver a intentar el proceso o salir del proceso."""
    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{ '='*50 }\nModificar sede\n{ '='*50 }" + Style.RESET_ALL)
        msede=input("\nIndique el nombre de la sede a modificar:").strip().capitalize()
        if msede in sedeP:
            new_name=input("\nIndique el nuevo nombre de la sede:").strip().capitalize()
            if new_name in sedeP:
                input(Fore.RED + Style.BRIGHT + "\nEl nuevo nombre de la sede ya existe. Presione Enter para continuar..." + Style.RESET_ALL)
                return
            elif not new_name:
                input(Fore.RED + Style.BRIGHT + "\nEl nombre de la sede no puede estar vacío. Presione Enter para continuar..." + Style.RESET_ALL)
                return
            else:
                index = sedeP.index(msede)
                sedeP[index] = new_name
                input(Fore.GREEN + Style.BRIGHT + "\nSede modificada con éxito. Presione Enter para continuar..." + Style.RESET_ALL)
                
        else:
            input(Fore.RED + Style.BRIGHT + f"\nLa sede '{msede}' no se encuentra en el sistema.\nPresione Enter para continuar..." + Style.RESET_ALL)
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        modificarSede()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(1)
        salir_aplicacion()
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        modificarSede()
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}" + Style.RESET_ALL)
        modificarSede()
        
def eliminarSede():
    """Función que permite eliminar una sede existente en el sistema. Solicita al usuario que ingrese el nombre de la sede a eliminar y verifica si existe en la lista de sedes. Si la sede se encuentra, se elimina de la lista y se muestra un mensaje de éxito. Si la sede no se encuentra, muestra un mensaje correspondiente y permite al usuario volver a intentar el proceso. Maneja excepciones para entradas inválidas y permite al usuario volver a intentar el proceso o salir del proceso.
    """
    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{ '='*50 }\nEliminar sede\n{ '='*50 }" + Style.RESET_ALL)
        esede=input("\nIndique el nombre de la sede a eliminar:").strip().capitalize()
        if esede in sedeP:
            sedeP.remove(esede)
            input(Fore.GREEN + Style.BRIGHT + f"\nLa sede '{esede}' ha sido eliminada del sistema. Presione Enter para continuar..." + Style.RESET_ALL)
        else:
            input(Fore.RED + Style.BRIGHT + f"\nLa sede '{esede}' no se encuentra en el sistema. Presione Enter para continuar..." + Style.RESET_ALL)
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        eliminarSede()
    except KeyboardInterrupt:
        input(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(1)
        salir_aplicacion()
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        eliminarSede()
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}" + Style.RESET_ALL)
        eliminarSede()
