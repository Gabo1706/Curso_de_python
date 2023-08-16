#la librería pandas hace el trabajo más profesional y sencillo
#Estos archivos son dataframes los cuales no son objetos normales
#Conceptualmente se pueden ver como hojas de cálculo ya que para acceder a ellos es necesario saber su ubicación(En otras palabras su fila y su columna)
import pandas as pd#se nombra "pd" porque así lo hacen universalmente
df=pd.read_csv("Archivos CSV\\prueba_CSV.csv",names=["Name","Last name","Age"])#Se usa el método read_csv
df2=pd.read_csv("Archivos CSV\\prueba_CSV.csv",names=["Name","Last name","Age"])#Se usa el método read_csv

#Obtener los datos de una columna
nombres=df["Age"] #Se indica el nombre de la columna


#Si se le quiere agregar una fila de titulos se usa el names= en la lectura del doc
#Al usarlo agrergamos los items de la lista names y la que teníamos se bajo a la siguiente fila

#ordenar datos por edad ascendente
orden_ascendente=df.sort_values("Age")


#Para descendente se declara el parámtero ascend como False
orden_descendente=df.sort_values("Age",ascending=False)

#Si en vez de poner el parametro "Age" ponemos "Name" los ordena por orden alfabético ascendente
#Si se quiere hacer alfabético descentente se hace el mismo proceso anterior

#Concatenar dataframes: se usa la función concat
#Recibe como parametros una lista que contenga los dataframes a concatenar
df_total=pd.concat([df,df2])

#Accediendo a las filas de arriba hacia abajo con  head(), se le indica cuantas filas quiere ver
primeras_filas=df_total.head(3)


#Accediendo a las últimas filas de arriba hacia abajo, se le indica cuantas filas quiere ver
ultimas_filas=df_total.tail(3)


#Accediendo al tamaño del doc con .shape
tamaño=df_total.shape
cantidad_filas,cantidad_columnas=tamaño# se desempaqueta así porque los valores que entrega.shape son tuplas

#Accediendo a la edad de la fila 2 con .loc
#.loc permite localizar cualquier elemento entregandole su ubicación
elemento_específico_loc=df.loc[2,"Age"]
df_total.index=range(df_total.shape[0])


#COMENTARIO
#Al concatenar dataframes los indices se guardan y eso puede ocacionar problemas
#La solución para reordenar los indices se encuentra en la línea 44
#En esta línea se uso el metodo.index que entrega los indices del dataframe
#Al igualarlo a un range nos muestra los indices entre 0 y el tamaño del dataframe

#Accediendo a la edad de la fila 2 con .iloc
#iloc en vez de recibir el nombre de la columna recibe el número de la fila y la columna
elemento_específico_iloc=df.iloc[2,2]


#Accediendo a filas y columnas enteras

fila_1=df_total.iloc[0,:]

columna_2=df_total.iloc[:,1]


#Se pueden poner condiciones adentro deel iloc
#Accediento solo a los mayores de 25 años

mas_de_25=df_total.loc[df_total["Age"]>25,:]
print(mas_de_25)


