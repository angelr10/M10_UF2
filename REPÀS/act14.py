numerosSucio = input("Introduce el contenido: ")
numerosLimpio = numerosSucio.split(" ")

#Proceso de ordenado

numerosOrdenados = []
vueltasNecesarias = len(numerosLimpio)

while True:
    if vueltasNecesarias >= 11 or vueltasNecesarias <= 9:
        numerosSucio = input("Introduce el contenido, necesitas 10 numeros separados: ")
        numerosLimpio = numerosSucio.split(" ")
        continue
    break

    

vueltaActual = 0
numeroActual = 0
verd = True
numerosLimpio.sort()
numerosLimpio = tuple(numerosLimpio) 
print(numerosLimpio)

#a = []
#a.append("x")
#a.append("Y")
#a = tuple(a)
#print(a)
'''
while True:#Bucle que recorra numerosLimpio y que obtiene el numero mas pequeño de toda la lista
    #si numerosLimpio es menor a 2 y si llegas al final
    if vueltasNecesarias <= 1:
        print(numerosLimpio[0])
        break
    if vueltaActual >= vueltasNecesarias:
        break
    
    #Condiciones de inicio
    if numerosLimpio[0] >= numerosLimpio[1] and verd == True:
        numeroActual = numerosLimpio[vueltaActual]
        vueltaActual = vueltaActual+1
        verd = False
        continue
    elif verd == True:
        numeroActual = numerosLimpio[vueltaActual]
  #      vueltaActual = vueltaActual+1
  #      verd = False
  #      continue
    
    #Condiciones continuas
 #   if verd == False and numeroActual >

#    vueltaActual = vueltaActual+1 
    '''