
'''
Este programa lee dos palabres y las añade a una
tupla para leer las veces que sale cada letra
'''
letraUno = input("Introduce la primera letra: ")
letraDos = input("Introduce la seguna letra: ")

#Unificamos y transformamos en tupla ambas palabras
fusion = letraUno+letraDos
trans1 = tuple(fusion)


#Añadimos primero
diccionario = {}
contadores = []
#diccionario.append(trans(0))
#contadores.append()

#Recorremos las palabras
for a in trans1:
    print(a)
    if a in diccionario:
        diccionario[a] += 1
    else:
        diccionario[a] = 1
    #Recorremos diccionario
    #for b in diccionario:

print(diccionario)