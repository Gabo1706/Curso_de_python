#Creando diccionarios con dict
#Se usa en especial para hacer diccionarios vacios
diccionario=dict(nombre="Gabriel",apellido="González") #se usa esta sintaxis


#los diccionarios no reciben listas, de modo que toca meter conjuntos o tuplas
#Creando diccionario de solo claves con fromkeys
#este método recibe un primer parametro de tipo iterable, cada parte de este elemento será la clave y automáticamente se le asignará valor none
diccionario=dict.fromkeys("ABCDE")
#Este método en su segundo parámetro recibe el valor que se le pondrá a todas las claves del primer parámetro (iterable)
diccionario2=dict.fromkeys("ABCDE","Valor fijo")
 