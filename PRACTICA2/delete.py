# Este archivo se necarga de eliminar
# el contenido creado anteriormente con el archivo
# create
sql_delete = ''' DELETE FROM public.COCHE WHERE user_id=1
'''

connection.execute(sql_delete)
conn.commit()