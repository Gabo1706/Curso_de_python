import pandas as pd
import matplotlib.pyplot as plt#librería para graficar
import seaborn as sns#Libreria pa cosas estadísticas

df=pd.read_csv("Archivos CSV\\ingresos.csv")
#mostrando gráfico de barras
sns.barplot(x="Fuente",y="Ingresos",data=df)

#si se requiere de sacar un total se usa el método sum

total_ingresos=df["Ingresos"].sum()

print(f"El total de ingresos de Gabriel son ${total_ingresos} USD")

plt.show()