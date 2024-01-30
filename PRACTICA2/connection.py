import psycopg2

conn = psycopg2.connect(
    database="M10/UF2/Databases/postgres",
    user='angel',
    password='angel',
    host='localhost',
    port='5432'
)

connection = conn.cursor()
print(connection)