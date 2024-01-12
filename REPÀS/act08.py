a = input("Agrega de 1 a 3 palabras a continuacion: ")
b = a.split()
while len(b)>3 or len(b)<1:
	print("Pls introduce un numero del 1 al 3")
	a = input("Agrega de 1 a 3 palabras a continuacion: ")
	b = a.split()
c = 0
while c < len(b):
	print("Has introducido : *"+str(b[c])+"* tiene un total de "+str(len(b[c]))+" caracteres, y comienza con el caracter *"+str(b[c][0:1])+"*, y finaliza con el caracter *"+str(b[c][-1])+"*")
	c=c+1
