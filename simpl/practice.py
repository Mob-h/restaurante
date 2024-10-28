with open('simpl/UIB.txt','r',encoding='utf-8') as archivo:
    contenido=archivo.readlines()
nuevalista=[]
for linea in contenido:
    if linea=='BB\n':
        resto=contenido[contenido.index(linea)+1::]
resto=''.join(resto)
nuevalista.append(resto)
print(nuevalista)
print(nuevalista[0])
#MANERA DE ACCEDER A DISTINTAS INTERFACEZ