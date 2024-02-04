#Este archivo python se encarga de actualizar
#la informaciona agregada en la tabla de COCHES
#
sql_update = ''' UPDATE public.COCHES SET coche_prop_nombre='NUEVO NOMBRE', coche_prop_edad=100, coche_matricula='11111111',coche_modelo='Ferrari',coche_color='rojo'
'''

connection.execute(sql_update)
conn.commit()
result = connection.rowcount
print("id modificada: ",result,"Actualizacion completada.")