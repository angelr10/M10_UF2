arraynumeros = []
tru = True
while tru:
    contenedorNumeros = input("Introduce un numero por favor(escribe 0 para terminar):")
    if int(contenedorNumeros) <= 0:
        print("Calculando...")
        tru = False
    else:
        arraynumeros.append(contenedorNumeros)
arraynumeros.sort()
arraynumeros = tuple(arraynumeros) 
print(arraynumeros)