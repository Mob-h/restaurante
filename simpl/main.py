#IMPORTS
import config
from funcionesPrincipales import *

#archivos interfazes
#FUNCT


#MAIN
"""PROGRAMA"""


config.limp()
while(config.appState != config.possibleStatesTupla[-1]):
    # Inicializacion 
    while True:
        if (config.loggedUserType == '' and config.appState == 'login'):
            config.tipoIngresado =input(config.ui[0])
            #DEBERIAMOS AGREGAR VALIDACION CON E.REGULARES COLO POR SI ESCRIBE CON CARACTERES
            if config.tipoIngresado=="1":
                config.tipoIngresado="cliente"
            elif config.tipoIngresado=="2":
                config.tipoIngresado="admin"
            elif config.tipoIngresado=="3":
                config.tipoIngresado="cocinero"
            elif config.tipoIngresado=="4":
                config.tipoIngresado="mesero"                
            config.limp()
        try:
            if verificarTipo(config.tipoIngresado)==False:
                raise ValueError
        except ValueError as ms:
            print(f'>> El usuario ingresado no existe, ingrese uno valido: {ms}')
        except Exception as error_mssg:
            print(f'Error : {error_mssg}')
        else:
            break
    config.loggedUserType = config.tipoIngresado
    config.loggedUserPermissions = getPermisos(config.loggedUserType)
    config.limp()
    config.appState=impresionPermisos(config.tipoIngresado,config.appState)
    # Verificacion de state
    while (config.appState not in config.possibleStatesTupla) | (verificarPermisos(config.appState,config.loggedUserPermissions) == False):
        config.limp()
        print('>>La opcion ingresada no es valido. Ingrese uno de los siguientes posibles')
        input(">>Enter para continuar")
        config.limp()
        config.appState=impresionPermisos(config.tipoIngresado,config.appState)
    config.limp()
    # Manejo de funcionalidades en base al state
    # ---Funcionalidad verPerfiles
    # ------- Pendiente validacion de inpu
    if config.appState == 'verPerfiles':
        
        while True:
            config.limp()
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
    if config.appState=="recepcion":
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
        
        if verificador_disponibilidad(cantidad_comensales,config.mesas):
            #entramos al if si solo la funcion verificador_disponibilidad devuelve true
            print(f"hay disponibilidad de mesas, la mesa es {config.id_mesa}")
            #modificamos el estado de la mesa buscandola por su id
            for elemento in config.mesas:
                if elemento["idMesa"]==config.id_mesa:
                    elemento["reserva"]=nombre
                    elemento["estado"]="reservado"
                    elemento["cantPersonas"]=cantidad_comensales
        else:
            print(">> No hay disponibilidad de mesas")       
        input('ENTER para continuar')
    if config.appState == 'verMesas':
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
            opcion=excepcionNumeroEnteros(config.ui[7])
            while opcion<1 or opcion>3:
                opcion=excepcionNumeroEnteros(config.ui[7])
            if opcion==1:
                reservar(nombre)
            elif opcion==2:
                verReservas(nombre)
            elif opcion==3:
                appState='login'
                break
    if config.appState=="pedidos":
        condicion_general=1
        while condicion_general==1:
            condicion=1
            opcion=menuAdminPedidos()
            config.limp()
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
                for elemento in config.pedidos:
                    contador+=1
                    print(f"{">>"}{("Pedido numero → "+str(contador)).center(55)}")
                    impresionPedidosIndividuales(elemento)
                config.limp()
            elif opcion==3:
                while condicion==1:
                    pedidos=administrarPedidos(config.pedidos)
                    #EXCEPCION
                    condicion=int(input("Seguir modificando pedidos 1/Si 2/No"))
                    config.limp()
            elif opcion==4:
                impresionRecetas(config.recetas)
                input("Enter para continuar")
                config.limp()
            elif opcion==5:
                inventario=solicitarIngredientes(config.inventario)
                input("Enter para continuar")
                config.limp()
            elif opcion==6:
                config.pedidos=repriorizarPedidos(config.pedidos)
                contador=0
                for elemento in config.pedidos:
                    contador+=1
                    print(f"{">>"}{("Pedido numero → "+str(contador)).center(55)}")
                    impresionPedidosIndividuales(elemento)  
                config.limp()
            elif opcion==7:
                condicion_general=0
                if (config.loggedUserType == 'cocinero' and config.appState == 'pedidos'):#solo para que el cocinero pueda salir al menu de perfiles
                    config.appState='login'
                    config.loggedUserType=''
                    config.loggedUserPermissions=None
    if (config.loggedUserType == 'mesero' and config.appState == 'finalizado'):#solo para que el mesero pueda salir al menu de perfiles
        config.appState='login'
        config.loggedUserType=''
        config.loggedUserPermissions=None
    # Finalizacion
    if(config.appState == config.possibleStatesTupla[-1]):
        config.appState='login'
        config.loggedUserType=''
        config.loggedUserPermissions=None

