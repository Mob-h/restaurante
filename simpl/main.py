#IMPORTS
from config import *
from funcionesPrincipales import *
from funcionesInicio import *
#archivos interfazes
#FUNCT


#MAIN
"""PROGRAMA"""


limp()
while(appState != possibleStatesTupla[-1]):
    # Inicializacion 
    while True:
        if (loggedUserType == '' and appState == 'login'):
            tipoIngresado =input(ui[0])
            #DEBERIAMOS AGREGAR VALIDACION CON E.REGULARES COLO POR SI ESCRIBE CON CARACTERES
            if tipoIngresado=="1":
                tipoIngresado="cliente"
            elif tipoIngresado=="2":
                tipoIngresado="admin"
            elif tipoIngresado=="3":
                tipoIngresado="cocinero"
            elif tipoIngresado=="4":
                tipoIngresado="mesero"                
            limp()
        try:
            if verificarTipo(tipoIngresado)==False:
                raise ValueError
        except ValueError as ms:
            print(f'>> El usuario ingresado no existe, ingrese uno valido: {ms}')
        except Exception as error_mssg:
            print(f'Error : {error_mssg}')
        else:
            break
    loggedUserType = tipoIngresado
    loggedUserPermissions = getPermisos(loggedUserType)
    limp()
    appState=impresionPermisos(tipoIngresado,appState)
    # Verificacion de state
    while (appState not in possibleStatesTupla) | (verificarPermisos(appState,loggedUserPermissions) == False):
        limp()
        print('>>La opcion ingresada no es valido. Ingrese uno de los siguientes posibles')
        input(">>Enter para continuar")
        limp()
        appState=impresionPermisos(tipoIngresado,appState)
    limp()
    # Manejo de funcionalidades en base al state
    # ---Funcionalidad verPerfiles
    # ------- Pendiente validacion de inpu
    if appState == 'verPerfiles':
        
        while True:
            limp()
            idPerfil = input('>> Ingrese all para ver todos los perfiles o el nombre exacto del userType: ')
            try:
                perfil = getPerfiles(idPerfil)
                if perfil == None:
                    raise ValueError
            except ValueError as ms:
                ms=str(ms)
                print(f'>> El valor ingresado no es correcto, error -> {ms}')
                input('>>ENTER para continuar')
            except Exception as error_mssg:
                error_mssg=str(error_mssg)
                print(f'>> Ha ocurrido un error: {error_mssg}')
                input('>>ENTER para continuar')
            else:
                break
        mostrarUserTypes(perfil)
    # ---Funcionalidad verMesas
    # ------- Pendiente validacion de input
    if appState=="recepcion":
        nombre=input(">> ingrese nombre de cliente :")
        while True:
            try:
                cantidad_comensales=int(input("ingrese la cantidad de comensales:"))
            except KeyboardInterrupt:
                print(f'>> Interrupcion detectada\n>> Finalizando..')
            except:
                print(f'>> Opcion no valida\n>> Ingrese una opcion valida')
                input('>> ENTER para continuar')
            else:
                break
        
        if verificador_disponibilidad(cantidad_comensales,mesas):
            #entramos al if si solo la funcion verificador_disponibilidad devuelve true
            print(f"hay disponibilidad de mesas, la mesa es {id_mesa}")
            #modificamos el estado de la mesa buscandola por su id
            for elemento in mesas:
                if elemento["idMesa"]==id_mesa:
                    elemento["reserva"]=nombre
                    elemento["estado"]="reservado"
                    elemento["cantPersonas"]=cantidad_comensales
        else:
            print(">> No hay disponibilidad de mesas")       
        input('ENTER para continuar')
    if appState == 'verMesas':
        #EXCEPCION        
        while True:
            try:
                idMesa = input('>>Ingrese all para ver todas las mesas o el id de la mesa: ').lower()
                mesa= getMesas(idMesa)
                if mesa==None:
                    raise ValueError
            except ValueError:
                print('>> Valor ingresado incorrecto')
                input('>> Enter para continuar')
            except Exception as ms:
                ms=str(ms)
                print('>> Ha ocurrido un error -> {ms}')
                input('>> Enter para continuar')
            else:
                break
        impresionMesas(mesa)
    if appState == 'operar':
        cliente()
    if appState == 'reservar':
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
            opcion=excepcionNumeroEnteros(ui[7])
            while opcion<1 or opcion>3:
                opcion=excepcionNumeroEnteros(ui[7])
            if opcion==1:
                reservar(nombre)
            elif opcion==2:
                verReservas(nombre)
            elif opcion==3:
                appState='login'
                break
    if appState=="pedidos":
        condicion_general=1
        while condicion_general==1:
            condicion=1
            opcion=menuAdminPedidos()
            limp()
            if opcion==1:
                while True:
                    try:
                        idMesa = input('>>Ingrese all para ver todas las mesas o el id de la mesa: ').lower()
                        mesa= getMesas(idMesa)
                        if mesa==None:
                            raise ValueError
                    except ValueError:
                        print('>> Valor ingresado incorrecto')
                        input('>> Enter para continuar')
                    except Exception as ms:
                        ms=str(ms)
                        print('>> Ha ocurrido un error -> {ms}')
                        input('>> Enter para continuar')
                    else:
                        break
                impresionMesas(mesa)                
            elif opcion==2:#salon
                contador=0
                for elemento in pedidos:
                    contador+=1
                    print(f"{">>"}{("Pedido numero → "+str(contador)).center(55)}")
                    impresionPedidosIndividuales(elemento)
                limp()
            elif opcion==3:
                while condicion==1:
                    pedidos=administrarPedidos(pedidos)
                    #EXCEPCION
                    condicion=int(input("Seguir modificando pedidos 1/Si 2/No"))
                    limp()
            elif opcion==4:
                impresionRecetas(recetas)
                input("Enter para continuar")
                limp()
            elif opcion==5:
                inventario=solicitarIngredientes(inventario)
                input("Enter para continuar")
                limp()
            elif opcion==6:
                pedidos=repriorizarPedidos(pedidos)
                contador=0
                for elemento in pedidos:
                    contador+=1
                    print(f"{">>"}{("Pedido numero → "+str(contador)).center(55)}")
                    impresionPedidosIndividuales(elemento)  
                limp()
            elif opcion==7:
                condicion_general=0
                if (loggedUserType == 'cocinero' and appState == 'pedidos'):#solo para que el cocinero pueda salir al menu de perfiles
                    appState='login'
                    loggedUserType=''
                    loggedUserPermissions=None
    if (loggedUserType == 'mesero' and appState == 'finalizado'):#solo para que el mesero pueda salir al menu de perfiles
        appState='login'
        loggedUserType=''
        loggedUserPermissions=None
    # Finalizacion
    if(appState == possibleStatesTupla[-1]):
        appState='login'
        loggedUserType=''
        loggedUserPermissions=None

