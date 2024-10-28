
import copy
import sys
from config import *
from funcionesPrincipales import *


#FUNCIONES EN RELACION A INICIO
def verificarTipo (type):
    tipoValido = False
    for userType in userTypes:
        if userType['userType'] == type:
            tipoValido = True
    return tipoValido
def getPermisos (type):
    for userType in userTypes:
        if userType['userType'] == type:
            return userType['permisos']
    else:
        return None
def verificarPermisos (state, permisos):
    stateValido = False
    for permiso in permisos:
        if permiso == state:
            stateValido = True
    return stateValido
def impresionPermisos(userType,appState):
    limp()
    if userType=="cliente":
        appState=input(ui[1])
        if appState=="1":
            appState="operar"
        elif appState=="2":#m
            appState="reservar"
        elif appState=="3":
            appState="finalizado"
    elif userType=="admin":
        appState=input(ui[2])
        if appState=="1":
            appState="verPerfiles"
        elif appState=="2":
            appState="verMesas"
        elif appState=="3":
            appState="pedidos"
        elif appState=="4":
            appState="finalizado"  
    elif userType=='cocinero':
        appState="pedidos"      
    elif userType=='mesero':
        appState=input(ui[3])    
        if appState=="1":
            appState="verMesas"
        elif appState=="2":
            appState="recepcion"
        elif appState=="3":
            appState="finalizado" 
    return appState
