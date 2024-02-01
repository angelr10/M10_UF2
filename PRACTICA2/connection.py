import psycopg2

#determina toda la informacion de la bd
conn = psycopg2.connect(
    database="postgres",
    user='angel',
    password='angel',
    host='localhost',
    port='5432'
)

#establece una conexion a la bd
connection = conn.cursor()
print(connection)