import copy
import sys
from config import *
from funcionesInicio import *

def getPerfiles (id):
    if id == 'all':
        return userTypes
    else:
        contenedorPerfil=[]
        for userType in userTypes:
            if userType['userType'] == id:
                contenedorPerfil.append(userType)
                return contenedorPerfil
    return None
def mostrarUserTypes(userTypes):
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║ {'Usuarios':<15}║{'Permisos':<45}║
╠══════════════════════════════════════════════════════════════╣""")
    for userType in userTypes:#va a recorrer la lista de dicts
        permisos = ', '.join(userType['permisos']).lower()#unifica los elementos de la clave "permisos"
        print(f"║ {userType['userType'].capitalize():<15}║{permisos:<45}║")
    print("╚══════════════════════════════════════════════════════════════╝")
    input(">>Enter para continuar\n")

def verificador_disponibilidad(cantidad_comensales,mesas):
    """variables"""
    for elemento in mesas:
        global id_mesa
        if elemento["maxPersonas"]>=cantidad_comensales and elemento["estado"]=="libre":
            #"si hay disponibilidad de mesas"
            id_mesa= elemento["idMesa"]
            return True
            #devuelve true y modifica el id de la mesa
    return False
def excepcionNumeroEnteros(mensaje):
    """Esta funcion tiene como fin manejar errores cuando el suusario debe ingresar un dato del tipo entero, retorna un entero"""
    variable=0
    while True:
        try:
            variable=int(input(mensaje))
        except ValueError:
            print(f'>> Opcion ingresada no valida\n>> Ingresar opcion valida')
        except Exception as ms:
            ms=str(ms)
            print(f'>> Ha ocurrido un error -> {ms}')
        else:
            break
    return variable



#FUNCIONES DE IMPRESION
def getMesas (id):
    if id == 'all':
        return mesas
    else:
        contenedorMesa=[]#para almacenar el diccionario mesa
        for mesa in mesas:
            if mesa['idMesa'] == id:
                contenedorMesa.append(mesa)
                return contenedorMesa
    return None
def impresionMesas(mesas):
    """
    Esta funcion recibe la estructutura de datos mesa y realiza una impresion
    la estructura debe contener una cantidad de mesas de numero PAR
    """
    if len(mesas)%2==0:
        print(f"""
╔═════════════════════════════════════════════╗
║                                             ║
║            🍽 RESTAURANTE🍽                   ║
║                   Mesas                     ║
║                                             ║""")
        for i in range(0,len(mesas),2):
            print(f"""╠═════════════════════════════════════════════╣
{"║":<2}{"Mesa →":<17}{(mesas[i]["idMesa"]):>4}{"║":<2}{"Mesa →":<17}{(mesas[i+1]["idMesa"]):>4}║
╠═════════════════════════════════════════════╣
{"║":<2}{"Estado →":<9}{(mesas[i]["estado"][0:12].capitalize()):>12}{"║":<2}{"Estado →":<9}{(mesas[i+1]["estado"][0:12].capitalize()):>12}║
{"║":<2}{"Reserva →":<9}{(mesas[i]["reserva"][0:12].capitalize()):>12}{"║":<2}{"Reserva →":<9}{(mesas[i+1]["reserva"][0:12].capitalize()):>12}║
{"║":<2}{"Personas →":<17}{(mesas[i]["cantPersonas"]):>4}{"║":<2}{"Personas →":<17}{(mesas[i+1]["cantPersonas"]):>4}║
{"║":<2}{"Limite →":<17}{(mesas[i]["maxPersonas"]):>4}{"║":<2}{"Limite →":<17}{(mesas[i+1]["maxPersonas"]):>4}║""")       
        input(f"╚═════════════════════════════════════════════╝\n>>Enter para continuar")      
    else:
        print(f"""
╔══════════════════════╗
║                      ║
║   🍽 RESTAURANTE🍽     ║
║         Mesas        ║
║                      ║""")
        for i in range(0,len(mesas)):
            print(f"""╠══════════════════════╣
{"║":<5}{"Mesa → ".center(12)}{mesas[i]["idMesa"]:<6}║
╠══════════════════════╣
{"║":<2}{"Estado →":<9}{(mesas[i]["estado"][0:12].capitalize()):>12}{"║":<2}
{"║":<2}{"Reserva →":<9}{(mesas[i]["reserva"][0:12].capitalize()):>12}{"║":<2}
{"║":<2}{"Personas →":<17}{(mesas[i]["cantPersonas"]):>4}{"║":<2}
{"║":<2}{"Limite →":<17}{(mesas[i]["maxPersonas"]):>4}{"║":<2}""")
       
        input(f"╚══════════════════════╝\n>>Enter para continuar")  
def impresionPedidosIndividuales(diccionario):

    print(f"""╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
{"║":<2}Pedidos de → {diccionario["nombre"].capitalize():<31}Mesa -> {diccionario["mesa"]:<2}║                    
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<3}║{'Plato':<28}║{'Cant':<4}║{'Estado':<17}║
╠═══════════════════════════════════════════════════════╣""")
    for plato in diccionario["platos"]:
        print(f"║{(diccionario["platos"].index(plato)+1):<3}║{plato[0]:<28}║{plato[1]:<4}║{plato[2]:<17}║")
    print("""╚═══════════════════════════════════════════════════════╝""")
    input("Presione Enter para continuar>>")
def impresionRecetas(recetas):
    i=0
    for elemento in recetas: #Imprime los nombres de las recetas
        print(f"{elemento.get("nombre")}")
    nombre=input("Ingrese nombre de plato: ").capitalize()
    limp()
    while i<len(recetas) and recetas[i].get("nombre")!=nombre:
        i=i+1
    if i>=len(recetas):
        print("nombre no encontrado")
    else: #Si encuentra el plato
        for clave,valor in recetas[i].items():
            if clave=="ingredientes":
                largo=len(recetas[i]["ingredientes"])
                for j in range(largo):
                    print(f"Ingrediente \"{j}\"={recetas[i+1]["ingredientes"][j]}")
            else:
                print(f"{clave} : {valor}")   
def mostrar_menu_platos(menu):
    limp()
    print(f"""
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
║                      Menu de platos                   ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<4}║{'Plato':<28}║{'Precio':<10}║{'Categoría':<10}║
╠═══════════════════════════════════════════════════════╣""")
    for plato in menu:
        print(f"║{(menu.index(plato)+1):<4}║{plato[0]:<28}║{plato[1]:<10}║{plato[2]:<9} {"║":<20}")
    print("""╚═══════════════════════════════════════════════════════╝""")
    input("Presione Enter para continuar>>")

def verPedidos(pedido):#recibe el pedido del cliente

    if len(pedido['platos']) > 0:#verifica que tenga pedidos
        impresionPedidosIndividuales(pedido)#llamada a funcion para imprimir diccionarios
        opcion = input("¿Desea cancelar algún pedido? (s/n): ").lower()
        if opcion == 's':
            numPedido = int(input("Ingrese el número de plato que desea cancelar: ")) - 1
            while numPedido<0 or numPedido>len(pedido):
                numPedido = int(input("Ingrese el número de plato que desea cancelar: ")) - 1
            del pedido["platos"][numPedido]
            print("Pedido cancelado.")
    else:
        print("Usted no tiene pedidos activos.")
    input("\nEnter para continuar")
     
def menuOpcionesAdministracion():
    while True:
        try:
            opcion = int(input(ui[6]))
            if opcion<1 or opcion>5:
                raise ValueError
        except ValueError:
            print(f'>> Opcion invalida, Ingrese una opcion valida')
            input('>> ENTER para continuar')
        except KeyboardInterrupt:
            print(f'>> Interrupcion detectada!\n>> Finalizando..')
            sys.exit(0)
        except Exception as ms:
            ms=str(ms)
            print(f'>> Ha ocurrido un error -> {ms}')
        else:
            break
    return opcion
def impresionInventario(inventario):
    for clave,valor in inventario.items():
        print(f"{clave}:{valor}")




#FUNCIONES DE CLIENTE
def client_menu():
    while True:
        try:
            limp()
            opcion = int(input(ui[5]))
            if opcion<1 or opcion>4:
                raise ValueError
        except ValueError:
            print(f'>>Opcion ingresada no valida\n>>Ingrese una valida')
            input('>> Enter para continuar')
        except Exception as ms:
            ms=str(ms)
            print(f'>> Ha ocurrido un error ->{ms}')
        else:
            break
    return opcion
def hacerPedido(nombre,pedido):
    listaAuxiliar=[]
    while True:
        try:
            plato = int(input("\nIngrese numero de plato (0 para terminar): "))
            if plato not in (list(range(0,13))):
                raise ValueError
        except ValueError:
            print(' >>Opcion ingresada no valida\n>> Ingrese una opcion valida')
        else:
            break
    while plato != 0:
        nombrePlato=menu[plato-1][0]
        while True:
            try:
                cant = int(input(f"Seleccione una cantidad (disponible {menu[plato-1][3]}): "))
                if cant > menu[plato-1][3]:
                    raise ValueError
            except ValueError:
                print(f'>> Opcion ingresada no valida\n>> Ingrese opcion valida')
            except Exception as ms:
                ms=str(ms)
                print(f'>>ha ocurrido un error -> {ms}')
            else:
                break
        if cant <= menu[plato-1][3]: #Si hay suficiente stock
            listaAuxiliar.clear()
            if len(pedido["platos"])>0:
                flag=True
                for elemento in pedido["platos"]:
                    if elemento[0]==nombrePlato:
                        flag=False
                        elemento[1]+=cant
                if flag:
                    listaAuxiliar.append(nombrePlato)
                    listaAuxiliar.append(cant)
                    listaAuxiliar.append("En preparacion")
                    pedido["platos"].append(listaAuxiliar.copy())
            else:
                listaAuxiliar.append(nombrePlato)
                listaAuxiliar.append(cant)
                listaAuxiliar.append("En preparacion")
                pedido["platos"].append(listaAuxiliar.copy())
        
            menu[plato-1][3] -= cant #Resta la cantidad pedida al stock                   
            print(f"Has agregado {cant} de {nombrePlato} a tu pedido.")
        while True:
            try:
                plato = int(input("\nIngrese numero de plato (0 para terminar): "))
                if plato not in (list(range(0,13))):
                    raise ValueError
            except ValueError:
                print(' >>Opcion ingresada no valida\n>> Ingrese una opcion valida')
            else:
                break            
    print("Gracias por su pedido!")
    input("\nEnter para continuar")
def cliente():
    listaIds=[]
    while True:
        try:
            nombre = input("Ingrese su nombre:\n>>").capitalize()
            if nombre=='' or nombre.isspace():
                raise ValueError
            if not(nombre.isalpha()):
                raise ValueError
        except ValueError:
            print(f'>> Opcion ingresada no valida\n>> Ingrese una valida')    
        else:
            break
    while True:
        try:
            numeroMesa=input('>> Ingrese numero de mesa')
            int(numeroMesa)
            listaIds=[mesa['idMesa'] for mesa in mesas]
            if numeroMesa not in listaIds:
                raise ValueError
            for mesa in mesas:
                if mesa['idMesa']==numeroMesa and mesa['estado']!='libre':
                    raise ValueError
        except ValueError:
            print(f'>> Opcion no valida, Ingrese una valida')
            input('ENTER para continuar')    
        except:
            print('>> Ha ocurrido un error')
            input('ENTER para continuar')
        else:
            break 
    pedido={"nombre":nombre,
            "mesa":numeroMesa,
            "platos":[]}
    opcion = client_menu()
    limp()
    while opcion !=4:    
        if opcion == 1:
            mostrar_menu_platos(menu)
            limp()
        elif opcion == 2:
            mostrar_menu_platos(menu)     
            hacerPedido(nombre,pedido)            
        elif opcion == 3:
            verPedidos(pedido)
        opcion=client_menu()
    limp()
    if len(pedido['platos'])>0:
        pedidos.append(copy.deepcopy(pedido))#UNA VEZ QUE EL CLIENTE CIERRA SESION, EL PEDIDO SE MANDA A LA ESTRUCTURA PRINCIPAL
    print("Gracias!")
def reservar(nombre):    
    impresionMesas(mesas)
    reserva=str(excepcionNumeroEnteros(f">>Que mesa quiere reservar?\n>>"))
    comensales=excepcionNumeroEnteros(f">>Para cuantas personas es la reserva?\n>>")
    mesaEncontrada = False
    reservado = False
    for mesa in mesas:
        #Verifico que la mesa sea valida y que haya elegido una libre
        if mesa["idMesa"] == reserva and mesa["estado"] == "libre":
            mesaEncontrada = True
            if comensales <= mesa["maxPersonas"]:
                #Si todo es correcto, actualizo la info de la mesa
                reservado = True
                mesa["estado"] = "reservado"
                mesa["reserva"] = nombre
                mesa["cantPersonas"] = comensales
                print(f"Mesa {reserva} reservada para {comensales} personas.")
            else:
                #Si quiere reservar para mas personas que la capacidad de la mesa
                print(f">>La mesa {reserva} tiene capacidad para {mesa['maxPersonas']} personas.")
            break
    if mesaEncontrada == False:
        #Se selecciono una mesa que no existe o que no esta libre
        print(">>La mesa solicitada no se encuentra disponible.")
    elif reservado == True:
        #Se realizo correctamente la reserva
        print(f"Gracias por su reserva, {nombre.capitalize()}")
    else:
        #Se intento reservar para mas personas que la capacidad de la mesa
        print("Reserva no realizada.")
    input("\nEnter para continuar")
def verReservas(nombre):
    reservasCliente = [mesa for mesa in mesas if mesa["reserva"] == nombre]#enlazamos si es que nuestro cliente tiene nombre, obtenemos una lista de diccionarios
    if len(reservasCliente) > 0:# si existe el diccionario que coincida con el nombre avanzamos
        print(f"Reservas de {nombre.capitalize()}:")
        impresionMesas(reservasCliente)
        opcion=excepcionNumeroEnteros(">> ¿Desea cancelar alguna reserva?\n>> 1 -> Si\n>> 2 -> No ")
        while (opcion !=1 and opcion!=2):
            print(">> Opcion invalida")
            opcion=excepcionNumeroEnteros(">> ¿Desea cancelar alguna reserva?\n>> 1 -> Si\n>> 2 -> No ")
        if opcion == 1:
            aux=[mesa["idMesa"] for mesa in reservasCliente]
            numMesa=str(excepcionNumeroEnteros(f"Ingrese el número de mesa de la reserva que desea cancelar: ")) 
            while numMesa not in aux:
                numMesa=str(excepcionNumeroEnteros(f"Ingrese el número de mesa de la reserva que desea cancelar: "))    
            for mesa in reservasCliente:
                if mesa["idMesa"]==numMesa:
                    mesa_cancelada=mesa
            mesa_cancelada["estado"] = "libre"
            mesa_cancelada["reserva"] = "sin reserva"
            mesa_cancelada["cantPersonas"] = 0
            print(f"Reserva de la Mesa {mesa_cancelada['idMesa']} cancelada.")
        else:
            pass
    else:
        print("No tiene reservas activas.")
    input("\nEnter para continuar")
  
  
  
  
#FUNCIONES DE COCINERO
def menuAdminPedidos():
    while True:
        try:
            opcion =int(input(ui[4]))
            if opcion<1 or opcion>7:
                raise ValueError
        except ValueError:
            print('>> Opcion ingresada no valida\n>> Ingrese una valida')
            input('>> Enter para continuar')
        except KeyboardInterrupt:
            print('\n>> Interrupción detectada..\n>> Terminando tareas..\n>> Finalizando..')
            sys.exit(0)
        except Exception as ms:
            ms=str(ms)
            print(f'>> Ha ocurrido un error -> {ms}')
            input('>> Enter para continuar')
        else:
            break
    return opcion
def administrarPedidos(pedidos):
    opcion=0
    contador=0
    for elemento in pedidos:
        contador+=1
        print(f"{">>"}{("Pedido numero → "+str(contador)).center(55)}")
        impresionPedidosIndividuales(elemento)
    while True:
        try:
            numPedido=int(input(">>Ingrese numero de pedido a modificar\n>> "))
            listaAuxiliarPedidos=list(range(1,len(pedidos)+1))
            if numPedido not in listaAuxiliarPedidos:
                raise ValueError    
        except ValueError:
            print('>> opcion ingresada no valida\n>> Ingrese una opcion valida')
        except KeyboardInterrupt:
            print(f'>> Interrupcion detectada\n>> Terminando tareas..\n>> Finalizando..')
            sys.exit(0)
        except Exception as ms:
            ms=str(ms)
            print('>> Ha ocurrido un error -> {ms}')
        else:
            break
    impresionPedidosIndividuales(pedidos[numPedido-1])
    while True:
        try:
            plato=int(input("ingrese numero de plato a modificar"))
            listaAuxiliar=list(range(1,len(pedidos[numPedido-1]["platos"])+1))
            if plato not in listaAuxiliar:
                #el valor ingresado como numero de plato no existe
                raise ValueError
        except ValueError:
            print('>> opcion ingresada no valida\n>> Ingrese numero de plato invalido')
        except KeyboardInterrupt:
            print(f'>> Interrupcion detectada\n>> Terminando tareas..\n>> Finalizando..')
            sys.exit(0)
        except Exception as ms:
            ms=str(ms)
            print('>> Ha ocurrido un error -> {ms}')
        else:
            break
    opcion=menuOpcionesAdministracion()
    #EXCEPCION EN CADA ACCESO
    if opcion==1:
        pedidos[numPedido-1]["platos"][plato-1][2]="Sin hacer"
    elif opcion==2:
        pedidos[numPedido-1]["platos"][plato-1][2]="En preparacion"
    elif opcion==3:
        pedidos[numPedido-1]["platos"][plato-1][2]="Listo"
    elif opcion==4:
        pedidos[numPedido-1]["platos"][plato-1][2]="Entregado"
    elif opcion==5:
        pedidos[numPedido-1]["platos"][plato-1][2]="Rechazado"
    return pedidos    
def solicitarIngredientes(inventario):
    impresionInventario(inventario)
    nombre=input("ingrese nombre del producto a agregar").capitalize()
    cantidad=int(input("ingrese cantidad a pedir"))
    """modificar ingredientes"""
    return inventario
def repriorizarPedidos(pedidos):
    contador=0
    for elemento in pedidos:
        contador+=1
        print(f"{">>"}{("Pedido numero → "+str(contador)).center(55)}")
        impresionPedidosIndividuales(elemento)
    # Solicito el numero del pedido que se desea mover y ajusto el indice
    numPedido = int(input("Ingrese el número de pedido que desea mover: ")) - 1
    # Verifico que el numero de pedido sea valido
    while numPedido < 0 or numPedido >= len(pedidos):
        print("Número de pedido inválido.")
        numPedido = int(input("Ingrese el número de pedido que desea mover: ")) - 1
    # Solicito la nueva posicion a la que se desea mover y ajusto el indice
    nuevaPos = int(input("Ingrese la nueva posición (1 para la primera): ")) - 1
    pedidoMovido = pedidos[numPedido]
    # Elimino el pedido de su posicion original
    pedidos = pedidos[:numPedido] + pedidos[numPedido + 1:]
    # Si la nueva posicion excede la longitud de la lista, lo agrego al final
    if nuevaPos >= len(pedidos):
        pedidos.append(pedidoMovido)
    # Si ingresa 0 o negativo, lo pone primero en la lista
    elif nuevaPos <= 0:
        pedidos = [pedidoMovido] + pedidos[:]
    else:
        # Inserto el pedido en la nueva posicion usando rebanado
        pedidos = pedidos[:nuevaPos] + [pedidoMovido] + pedidos[nuevaPos:]
    print("Repriorización hecha.")  
    return pedidos