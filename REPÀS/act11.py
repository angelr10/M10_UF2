numero = input("Introduce un numero del 10 al 100: ")
if int(numero) > 100 or int(numero) < 10:
	numero = input("Introduce un numero del 10 al 100 valido:")
tuplaA = ()
tuplaA = tuple(range(1,int(numero)))
print(tuplaA)
