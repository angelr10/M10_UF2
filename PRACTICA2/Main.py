import psycopg2
import create.py
connection.execute()
a = input("Quieres crear la base de datos?")
if a == "si":
    exec(open('create.py').read())
    print("Base de datos creada")
else:
    print("No se ha creado la base de datos")