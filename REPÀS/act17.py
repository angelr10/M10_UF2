
'''
Este programa lee una frase introducida por el 
usuario, y registra solamente la primera letra 
de la frase.
ejemplo:
    caracteristica
    carteis
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
print("fin")
print(diccionarioEncontrado)
