#Para poder acceder a los modulos hay que hacer un correcto recorrido de las carpetas.
#en el caso de que el modulo a importar este en una carpeta en la misma ruta se llama de la siguiente manera:

'''import modulos1_saludo 
saludo=modulos1_saludo.saludo("Gabriel")
print(saludo)'''

#El anterior caso no funciona porque no se encuentra en la ruta correcta, la manera correcta sería:
#Este es el caso en el que se encuentren en la misma carpeta
#enrutamiento y la carpeta modulos ejemplo se encuentran en la carpeta modulos
'''import modulos_ejemplo.modulos1_saludo
saludo =modulos_ejemplo.modulos1_saludo.saludo("Gabriel")'''

#En el caso de que los modulos no estén en la misma carpeta es necesario agregar la ruta 
#para ver la ruta se usa el método path
import sys

#sys muestra los modulos hechos por Python. se usa dir para saber que metodos contiene dicho modulo
#entre esos aparece path

#aAcá devuelve las rutas en una lista, entonces para agregar la ruta deseada se hace:
sys.path.append('C:\\Users\\ASUS\\Desktop\\Curso de Python')# sin esta línea no funciona el código ya que es la que permite acceder al modulo deseado
import modulos1_saludo
saludo=modulos1_saludo.saludo("Gabriel")
print(saludo) 