#En este caso se agrega el parametro "a" para indicar que se van a agregar cosas
with open("Archivos TXT\\Prueba_TXT.txt","a",encoding="UTF-8") as archivo:
    archivo.writelines(["Esto es lo agregado\n","Esto es lo segundo agregado"])
#el .write agrega lo que se le indica cada vez que se corre el código

#RECORDATORIO .write recibe string, .writelines recibe iterables (Listas)