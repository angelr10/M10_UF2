numero = input("Introduce un numero del 1 al 10: ")
resultado = 0
while True:
	if int(numero)>= 0 and int(numero)<=10:
		break
	else:
		numero = input("introduce un numero valido, del 1 al 10: ")

for i in range (11):
	resultado=int(numero)*int(i)
	print(str(resultado)+",",end='')
