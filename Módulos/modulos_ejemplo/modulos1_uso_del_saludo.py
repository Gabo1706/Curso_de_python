#Acá importaremos el doc modulos1_saludo

import modulos1_saludo
saludo= modulos1_saludo.saludo("Gabriel")
print(saludo)

#También se puede importar una función en específico de un modulo conla función from
#Si quiere traer varias funciones las pide separándolas con comas
#EJEMPLO: from modulos1_saludo import funcion1,funcion2 

from modulos1_saludo import saludo
saludo=saludo("Gabriel")
print(saludo)

#En el caso de que el nombre del modulo incomode en el código se puede cambiar con la función as
#ejemplo importmodulos1_saludo as saludos
#el as también se puede usar para renombrar las funciones

import modulos1_saludo as saludos
saludo_normal=saludos.saludo("Gabriel")
print(saludo_normal)