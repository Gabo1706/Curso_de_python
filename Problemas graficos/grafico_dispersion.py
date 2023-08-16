import pandas as pd
import matplotlib.pyplot as plt#librería para graficar
import seaborn as sns#Libreria pa cosas estadísticas

df=pd.read_csv("Archivos CSV\\dispersión.csv")

sns.scatterplot(x="Tiempo",y="Dinero",data=df)


plt.show()