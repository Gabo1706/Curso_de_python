# Para leer un documento toca usar la función open 
#Es necesario poner el enrutamiento para que sepa que archivo abrir
#El enrutamiento se separa con backslashes, se pone el nombre con su extension .txt
#Se pone encodign UTF-( para que se puedan leer todos los caracteres sin error)
archivo_sin_leer=open("Archivos TXT\\Prueba_TXT.txt",encoding="UTF-8")

#Leer el archivo completo
#Se usa el metodo .read para leer el archivo y guardarlo en una variable
#La variable "archivo_sin_leer" solo tenía la función de abrir dicho archivo y almacenarlo, no leerlo
#archivo=archivo_sin_leer.read()

#Leer solo una línea
#si se usa el método readlines se leen todas las líneas
linea=archivo_sin_leer.readline()#el número que se meta en el método indica la cantidad de caracteres que se desean leer
print(linea)

#OBSERVACIÓN
#El código no funcionó porque antes tenía una línea que daba la orden de leer
#al tener un read antes del readline no funciona correctamente porque no se puede leer varias veces el mismo doc

#Siempre que se abra un archivo es necesario cerrarlo con .close
archivo_sin_leer.close

#Al cerrarlo no se puede leer abajo sin haberlo abierto de nuevo
 