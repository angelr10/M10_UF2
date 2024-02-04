# Este fichero se encarga de hacer la lectura de la base
# de datos de la informacion agregada a la tabla
sql_insert = ''' SELECT coche_prop_nombre, coche_prop_edad, coche_matricula,coche_modelo,coche_color
                    FROM public.COCHES
'''

connection.execute(sql_insert)
result = connection.fetchall()

for i in result:
    print("coche_prop_nombre",i[0],)
    print("coche_prop_edad",i[1],)
    print("coche_matricula",i[2],)
    print("coche_modelo",i[3],)
    print("coche_color",i[4],)