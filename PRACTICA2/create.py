# Este archivo contiene las ordenes para 
# crear un insert de informacion dentro de la base 
# de datos.
sql_insert = ''' INSERT INTO public.COCHES(coche_prop_nombre, coche_prop_edad, coche_matricula,coche_modelo,coche_color)
                VALUES('1',22,'88888888','subaru','azul')
'''

connection.execute(sql_insert)
conn.commit()