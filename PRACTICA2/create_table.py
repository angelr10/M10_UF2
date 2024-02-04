#Este fichero se encarga de generar una orden que reciba la base de datos indicandole que genere una tabla

sql = '''CREATE TABLE COCHES(
    coche_id SERIAL PRIMARY KEY,
    coche_prop_nombre VARCHAR(255) NOT NULL,
    coche_prop_edad TINYINT NOT NULL
    coche_matricula CHAR(8) NOT NULL
    coche_modelo VARCHAR(40) NOT NULL,
    coche_color VARCHAR(15) NOT NULL
)
'''
print("Se ha creado la tabla TABLE")

connection.execute(sql)
print(connection)
connection.commit()