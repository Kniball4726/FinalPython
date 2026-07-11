import os, time
from colorama import Fore, Style
from src.helpers.helper import salir_aplicacion

menu:list=[]
opcion:str=""
dni:int=0
user:str=""
password:str=""
usuarios:dict={}
submenu:list=[]


pedidos = {
    23456: {
            "cliente": "Ruben blale",
            "bultos": 3,
            "Sedes": "Pasteur",
            "logistica": "Transporte Sur",
            "operario": "Juan Pérez",
            "productos": [
                {"producto": "Whey protein 2lbs chocolate", "cantidad": 10},
                {"producto": "Creatine 500 gr", "cantidad": 20}
            ]
        }
    }


def borrarPantalla():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def buscarPedido(sede=None):
    """Función que permite buscar un pedido por su número de remito. Solicita al usuario que ingrese el número de remito y verifica si existe en el diccionario de pedidos. Si se encuentra, muestra los detalles del pedido, incluyendo cliente, bultos, logística, operario y productos asociados. Si no se encuentra, muestra un mensaje indicando que el pedido no fue encontrado en la sede correspondiente. Maneja excepciones para entradas inválidas y permite al usuario volver a intentar la búsqueda o salir del proceso.
    
    """
    remito:int=0

    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{'='*50}\nBuscar Pedido - Sede: {sede}\n{'='*50}" + Style.RESET_ALL)
        remito=int(input("\nIndique remito a buscar: "))
       
        if remito in pedidos.keys() and (sede is None or pedidos[remito].get('Sedes') == sede):
            print(Fore.GREEN + Style.BRIGHT + f"\n✓ Pedido Encontrado" + Style.RESET_ALL)
            print(f"\n{'='*50}")
            print(f"Pedido {remito}:")
            print(f"{'='*50}")
            print(f"Cliente: {pedidos[remito]['cliente']}")
            print(f"Bultos: {pedidos[remito]['bultos']}")
            print(f"Sede: {pedidos[remito].get('Sedes', 'No definida')}")
            print(f"Logística: {pedidos[remito]['logistica']}")
            print(f"Operario: {pedidos[remito]['operario']}")
            print(f"\nProductos:")
            for prod in pedidos[remito]['productos']:
                print(f"  - {prod['producto']}: {prod['cantidad']} unidades")
            input("\nPresione para continuar . . .")
            borrarPantalla()
            return True
        else:
            input(Fore.RED + Style.BRIGHT + "\n✗ Pedido no encontrado en su sede" + Style.RESET_ALL)
            borrarPantalla()
            return False

    except TypeError:
        input("\nError en el tipo de datos")
        buscarPedido(sede)
    except ValueError:
        input("\nIndique un número valido")
        buscarPedido(sede)
    except KeyboardInterrupt:
        print("\nSaliendo . . .")
        time.sleep(2)
        salir_aplicacion()
    except Exception as e:
        input(f"Error: {e}")
        salir_aplicacion()



def agregarPedido(sede:str):
    """Función que permite agregar un nuevo pedido al sistema. Solicita al usuario que ingrese los detalles del pedido, incluyendo remito, cliente, cantidad de bultos, logística, operario y productos asociados. Los productos se ingresan en un bucle, permitiendo al usuario agregar múltiples productos con sus cantidades correspondientes. Una vez ingresados todos los datos, el pedido se almacena en el diccionario de pedidos. Maneja excepciones para entradas inválidas y permite al usuario volver a intentar el proceso de agregar un pedido o salir del proceso.
    """
    remito:int=0
    cliente:str=""
    bultos:int=0
    logistica:str=""
    operario:str=""
    cantprod:int=0
    productos_lista:list=[]
    global pedidos

    try:    
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{'='*50}\nAgregar Pedido - Sede: {sede}\n{'='*50}" + Style.RESET_ALL)
        remito=int(input("\nIndique remito: "))
        cliente=input("Indique cliente: ").strip().capitalize()
        bultos=int(input("Indique cantidad de bultos: "))
        logistica=input("Indique logistica: ").strip().capitalize()
        operario=input("Indique operario: ").strip().capitalize()
        cantprod=int(input("Cuantos articulos lleva el remito? "))
        productos_lista = []
       
        for numeros in range(cantprod):
            print(f"Producto {numeros+1} de {cantprod}\n")
            productos=input("\nIndique nombre de producto: ")
            cantidades=int(input("Indique cantidades: "))
            prod = {"producto": productos, "cantidad": cantidades}
            productos_lista.append(prod)

        pedidos[remito]={
                "cliente":cliente,
                "bultos":bultos,
                "logistica":logistica,
                "operario":operario,
                "Sedes": sede,
                "productos": productos_lista
        }

        print(Fore.GREEN + Style.BRIGHT + f"✓ Pedido Registrado" + Style.RESET_ALL)
        print(f"\n{'='*50}")
        print(f"Pedido {remito}:")
        print(f"{'='*50}")
        print(f"Cliente: {pedidos[remito]['cliente']}")
        print(f"Bultos: {pedidos[remito]['bultos']}")
        print(f"Logística: {pedidos[remito]['logistica']}")
        print(f"Operario: {pedidos[remito]['operario']}")
        print(f"\nProductos:")
        for prod in pedidos[remito]['productos']:
            input(f"  - {prod['producto']}: {prod['cantidad']} unidades")


    except TypeError:
        input("\nError en el tipo de datos")
        agregarPedido(sede)
    except ValueError:
        input("\nIndique un número valido")
        agregarPedido(sede)
    except KeyboardInterrupt:
        print("\nSaliendo . . .")
        time.sleep(1)
        salir_aplicacion()
    except Exception as e:
        input(f"\nOcurrió un error: {e}")
        agregarPedido(sede)


def verPedidos(sede:str):
    """Función que permite ver todos los pedidos registrados en el sistema para una sede específica. Filtra los pedidos por la sede proporcionada y muestra los detalles de cada pedido, incluyendo remito, cliente, cantidad de bultos, logística, operario y productos asociados. Si no se encuentran pedidos para la sede especificada, muestra un mensaje indicando que no hay registros. Maneja excepciones para entradas inválidas y permite al usuario volver a intentar el proceso de visualización o salir del proceso."""
    global pedidos
    borrarPantalla()
    pedidos_sede = [datos for datos in pedidos.values() if datos.get('Sedes') == sede]

    if pedidos_sede:
        print(Fore.GREEN + Style.BRIGHT + f"{ '='*50 }\nLista de pedidos registrados - Sede: {sede}\n{ '='*50 }" + Style.RESET_ALL)
        for remito, datos in pedidos.items():
            if datos.get('Sedes') != sede:
                continue
            print(f"\nPedido {remito}:")
            print(f"Cliente: {datos['cliente']}")
            print(f"Bultos: {datos['bultos']}")
            print(f"Logística: {datos['logistica']}")
            print(f"Operario: {datos['operario']}")
            print(f"Sede: {datos['Sedes']}")
            print(f"Productos:")
            for prod in datos['productos']:
                print(f"  - {prod['producto']}: {prod['cantidad']} unidades")
            print()
    else:
        print("No se encontraron registros para la sede seleccionada")
    input("\nPresione una tecla para volver . . .")
    
def modificarPedido(sede:str):
    """Función que permite modificar los datos de un pedido existente en el sistema. Solicita al usuario que ingrese el número de remito del pedido a modificar y verifica si existe en el diccionario de pedidos. Si se encuentra, muestra los detalles actuales del pedido y permite al usuario seleccionar qué campo desea modificar: cliente, bultos, logística, operario o productos asociados. Los productos se pueden agregar, modificar o eliminar mediante un submenú. Una vez realizados los cambios, el pedido se actualiza en el diccionario de pedidos. Maneja excepciones para entradas inválidas y permite al usuario volver a intentar el proceso de modificación o salir del proceso.
    """
    global pedidos
    remito: int = 0
   
    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{'='*50}\nModificar Pedido - Sede: {sede}\n{'='*50}" + Style.RESET_ALL)
        remito = int(input("\nIndique remito a modificar: "))
       
        if remito in pedidos.keys() and pedidos[remito].get('Sedes') == sede:
            # Mostrar datos actuales
            print(f"\nPedido {remito}:")
            print(f"Cliente: {pedidos[remito]['cliente']}")
            print(f"Bultos: {pedidos[remito]['bultos']}")
            print(f"Logística: {pedidos[remito]['logistica']}")
            print(f"Operario: {pedidos[remito]['operario']}")
            print(f"\nProductos:")
            for prod in pedidos[remito]['productos']:
                print(f"  - {prod['producto']}: {prod['cantidad']} unidades")
           
            # Menú de modificación
            borrarPantalla()
            print("\n¿Qué desea modificar?")
            print("1. Cliente")
            print("2. Bultos")
            print("3. Logística")
            print("4. Operario")
            print("5. Productos")
            print("0. Cancelar")
           
            opcion = input("\nSeleccione opción: ")
           
            match opcion:
                case "1":
                    pedidos[remito]['cliente'] = input("Nuevo cliente: ").strip().capitalize()
                    input(Fore.GREEN + Style.BRIGHT + "\nCliente modificado exitosamente" + Style.RESET_ALL)
                case "2":
                    pedidos[remito]['bultos'] = int(input("Nueva cantidad de bultos: "))
                    input(Fore.GREEN + Style.BRIGHT + "\nBultos modificados exitosamente" + Style.RESET_ALL)
                case "3":
                    pedidos[remito]['logistica'] = input("Nueva logística: ").strip().capitalize()
                    input(Fore.GREEN + Style.BRIGHT + "\nLogística modificada exitosamente" + Style.RESET_ALL)
                case "4":
                    pedidos[remito]['operario'] = input("Nuevo operario: ").strip().capitalize()    
                    input(Fore.GREEN + Style.BRIGHT + "\nOperario modificado exitosamente" + Style.RESET_ALL)
                case "5":
                    modificarProductosPedido(remito)
                case "0":
                    return
                case _:
                    input("\nOpción no válida")
                    time.sleep(1)
        else:
            input(Fore.RED + Style.BRIGHT + "\nPedido no encontrado en su sede" + Style.RESET_ALL)
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido" + Style.RESET_ALL)
        modificarPedido(sede)
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido" + Style.RESET_ALL)
        modificarPedido(sede)
    except KeyboardInterrupt:
        print("\nSaliendo . . .")
        time.sleep(1)
        salir_aplicacion()
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}\nPresione Enter para continuar..." + Style.RESET_ALL)
        modificarPedido(sede)

def modificarProductosPedido(remito):
    """Función para modificar los productos de un pedido de forma numerada."""
    global pedidos
   
    try:
        while True:
            borrarPantalla()
            print(f"\n{'='*50}")
            print(f"Modificar Productos del Pedido {remito}")
            print(f"{'='*50}")
            print("\nProductos actuales:")
           
            if not pedidos[remito]['productos']:
                input("No hay productos registrados")
            else:
                for i, prod in enumerate(pedidos[remito]['productos'], 1):
                    print(f"  {i}. {prod['producto']}: {prod['cantidad']} unidades")
               
            borrarPantalla()
            print("\n¿Qué desea hacer?")
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. Eliminar producto")
            print("0. Volver")
           
            op = input("\nSeleccione opción: ").strip()
           
            match op:
                case "1":
                    # Agregar nuevo producto
                    productos = input("\nIndique nombre de producto: ").strip()
                    cantidades = int(input("Indique cantidad: "))
                    prod = {"producto": productos, "cantidad": cantidades}
                    pedidos[remito]['productos'].append(prod)
                    input(Fore.GREEN + Style.BRIGHT + "\n✓ Producto agregado exitosamente" + Style.RESET_ALL)
                case "2":
                    # Modificar producto existente
                    if not pedidos[remito]['productos']:    
                        input(Fore.RED + Style.BRIGHT + "\nNo hay productos para modificar" + Style.RESET_ALL)
                        continue
                    num = int(input(f"\nIndique número del producto a modificar (1-{len(pedidos[remito]['productos'])}): "))
                    if 1 <= num <= len(pedidos[remito]['productos']):
                        idx = num - 1
                        print(f"\nProducto actual: {pedidos[remito]['productos'][idx]['producto']}")
                        print(f"Cantidad actual: {pedidos[remito]['productos'][idx]['cantidad']}")
                        nuevo_nombre = input("Nuevo nombre (presione Enter para mantener): ").strip()
                        nueva_cantidad = input("Nueva cantidad (presione Enter para mantener): ").strip()
                        if nuevo_nombre:
                            pedidos[remito]['productos'][idx]['producto'] = nuevo_nombre
                        if nueva_cantidad:
                            pedidos[remito]['productos'][idx]['cantidad'] = int(nueva_cantidad)
                        input(Fore.GREEN + Style.BRIGHT + "\n✓ Producto modificado exitosamente" + Style.RESET_ALL)
                    else:
                        input(Fore.RED + Style.BRIGHT + "\nNúmero de producto no válido" + Style.RESET_ALL)
                case "3":
                    # Eliminar producto
                    if not pedidos[remito]['productos']:
                        input(Fore.RED + Style.BRIGHT + "\nNo hay productos para eliminar" + Style.RESET_ALL)
                        continue
                    num = int(input(f"\nIndique número del producto a eliminar (1-{len(pedidos[remito]['productos'])}): "))
                    if 1 <= num <= len(pedidos[remito]['productos']):
                        idx = num - 1
                        producto_eliminado = pedidos[remito]['productos'].pop(idx)
                        input(Fore.GREEN + Style.BRIGHT + f"\n✓ Producto '{producto_eliminado['producto']}' eliminado exitosamente" + Style.RESET_ALL)
                    else:
                        input(Fore.RED + Style.BRIGHT + "\nNúmero de producto no válido" + Style.RESET_ALL)
                case "0":
                    print("\nVolviendo al menú anterior...")
                    input("\nPresione Enter para continuar...")
                    break
                case _:
                    input(Fore.RED + Style.BRIGHT + "\nOpción no válida" + Style.RESET_ALL)
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido" + Style.RESET_ALL)
        modificarProductosPedido(remito)
    except TypeError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido" + Style.RESET_ALL)
        modificarProductosPedido(remito)
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}\nPresione Enter para continuar..." + Style.RESET_ALL)
        modificarProductosPedido(remito)
    except KeyboardInterrupt:
        input(Fore.RED+Style.BRIGHT+"\n\nSaliendo . . ."+Style.RESET_ALL)
        salir_aplicacion()
        
def eliminarPedido(sede:str):
    """Función que permite eliminar un pedido existente en el sistema. Solicita al usuario que ingrese el número de remito del pedido a eliminar y verifica si existe en el diccionario de pedidos. Solo elimina pedidos de la sede de sesión."""
    global pedidos
    remito: int = 0
   
    try:
        borrarPantalla()
        print(Fore.GREEN + Style.BRIGHT + f"{'='*50}\nEliminar Pedido - Sede: {sede}\n{'='*50}" + Style.RESET_ALL)
        remito = int(input("\nIndique remito a eliminar: "))
       
        if remito in pedidos.keys() and pedidos[remito].get('Sedes') == sede:
            # Mostrar datos del pedido a eliminar
            print(f"\n{'='*50}")
            print(f"Pedido a Eliminar - Remito {remito}:")
            print(f"{'='*50}")
            print(f"Cliente: {pedidos[remito]['cliente']}")
            print(f"Bultos: {pedidos[remito]['bultos']}")
            print(f"Logística: {pedidos[remito]['logistica']}")
            print(f"Operario: {pedidos[remito]['operario']}")
            print(f"\nProductos:")
           
            for prod in pedidos[remito]['productos']:
                print(f"  - {prod['producto']}: {prod['cantidad']} unidades")
           
            # Pedir confirmación
            print(f"{'='*50}")    
            print("\n¿Está seguro de que desea eliminar este pedido?")
            confirmacion = input("Escriba 'S' para confirmar o 'N' para cancelar: ").strip().upper()
           
            if confirmacion == "S":
                del pedidos[remito]
                input(Fore.GREEN + Style.BRIGHT + "\nPedido eliminado exitosamente" + Style.RESET_ALL   )
                
            elif confirmacion == "N":
                input(Fore.RED + Style.BRIGHT + "\nOperación cancelada" + Style.RESET_ALL)
            else:
                input(Fore.RED + Style.BRIGHT + "\nOpción no válida" + Style.RESET_ALL)

            input("\nPresione una tecla para continuar . . .")
            
        else:
            input(Fore.RED + Style.BRIGHT + "\nPedido no encontrado en su sede" + Style.RESET_ALL)
            
    except ValueError:
        input(Fore.RED + Style.BRIGHT + "\nIndique un número válido" + Style.RESET_ALL)
        eliminarPedido(sede)
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\n\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(1)
        salir_aplicacion()
    except Exception as e:
        input(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}\nPresione Enter para continuar..." + Style.RESET_ALL)
        eliminarPedido(sede)
