#PROBLEMA 1
#Cambiar el tipo de dato de una columna
import pandas as pd
df=pd.read_csv("Archivos CSV\\prueba_CSV.csv")
df["Age"]=df["Age"].astype(str) #astype cambia el tipo de valor

#Reemplazando datos de un arreglo usando replace
#El primer parámetro indica que valor reemplazar y el segundo indica con cual reemplazarlo
#Se debe poner el inplpace=True para que funcione
df.replace("Gonzalez","Ramirez",inplace=True)

#Eliminar filas o columnas con datos faltantes con dropna
df=df.dropna()#aca elimina filas
#df=df.dropna(axis=1)#acá elimina columnas


#Eliminar filas repetidas con drop_duplicates
df=df.drop_duplicates()


#Crear un CSV a partir de un dataframe creado (limpio)
df.to_csv("Resolver_problemas\\CSV_limpio_creado.csv")



