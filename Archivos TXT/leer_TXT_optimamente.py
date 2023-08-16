#Para leerlo de mejor manera usando menos recursos se usa with open de la siguiente manera
with open("Archivos TXT\\Prueba_TXT.txt",encoding="UTF-8") as archivo:
    print(archivo.read())
    #No es necesario cerrar el archivo usando with open