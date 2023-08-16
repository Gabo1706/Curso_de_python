#Usamos la librería CSV
import csv

#Se abre el docuemtno como con los archivos tipo TXT
with open("Archivos CSV\\prueba_CSV.csv") as archivo_csv:
    #para leer el archivo se usa la funcionón csv.reader
    reader=csv.reader(archivo_csv)
    #No se puede leer directamente con el print ya que es un objeto, entonces podemos recorrerlo con bucles
    for fila in reader:
        print(fila)
    #Cada item que recorre el for es una fila y lo entrega en forma de lista    