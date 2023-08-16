import pandas as pd
import matplotlib.pyplot as plt#librería para graficar
import seaborn as sns#Libreria pa cosas estadísticas

df=pd.read_csv("Archivos CSV\\Fecha,Barras.csv")

sns.lineplot(x="Fecha",y="Barras",data=df)

plt.plot("01/11",70,"o")#Agregando un punto a la gráfica
#Si el término no se encuentra automáticamente se crea el punto como nuevo dato del dataframe

plt.show()