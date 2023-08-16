#En este caso se agregó el parametro w para indicarle que usaremos permisos de escritura
#Cuando se pone w se SOBREESCRIBE sobre el archivo existente y solo queda lo que quiere ingresar
#Si se quieren agregar varias líneas se ingresa una lista
#Tiene la función inversa de readlines ya que readlines lee y entrega una lista con las líneas
#En cambio writelines recibe una lista con las líneas y las escribe
with open("Archivos TXT\\Prueba_TXT.txt","w",encoding="UTF-8") as archivo:
    archivo.writelines("Esto es nuevo")
    archivo.writelines(["\nesto es lo segundo nuevo\n","Estos es lo tercero nuevo"])# el \n indica salto de línea
