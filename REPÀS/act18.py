
'''
Este programa lee dos palabres y las añade a una
tupla para leer las veces que sale cada letra
'''
entrada = input("Introduce una frase: ")
entrada.split(" ")
entrada = tuple(entrada)

diccionarioEncontrado = []
vueltaSecundaria = 0
vueltaPrimaria = 0

#Bucle que recorra cada uno de los
#caracteres en busca de nuevos
#print(entrada[1])
bucleLectura = 0

if len(entrada) >= 1:
    diccionarioEncontrado.append(entrada[0])
    caracterActual=entrada[bucleLectura]
while True:
    if bucleLectura >= len(entrada):
        break
    intDentroFor=0
    while True:
        if intDentroFor == len(diccionarioEncontrado):
            diccionarioEncontrado.append(entrada[bucleLectura])
            break
        #print(len(diccionarioEncontrado))
        if diccionarioEncontrado[int(intDentroFor)] == entrada[int(bucleLectura)]:
            break
        intDentroFor=intDentroFor+1
    bucleLectura=bucleLectura+1
#OBTENEMOS EL diccionario de letras
intFueraOut=0
while True:#Pasamos por el diccionario
    if intFueraOut >= len(diccionarioEncontrado):
        break
    intDentroSub=0
    intLetraVecesEncontrada=0
    while True:#Pasamos por el texto
        print(intDentroSub)
        if intDentroSub >= len(entrada):
            print("La letra ",diccionarioEncontrado[intFueraOut]," ha sido encontrada ",intLetraVecesEncontrada," veces.")
        if entrada[intDentroSub] == diccionarioEncontrado[intFueraOut]:
            intLetraVecesEncontrada=intLetraVecesEncontrada+1
        intDentroSub=intDentroSub+1

    intFueraOut=intFueraOut+1


print("fin")