#Punto a

texto=input("Por favor escriba su texto aquí: ")
lista_palabras=texto.split(" ")
cantidad_palabras=len(lista_palabras)
tiempo_hablando=cantidad_palabras*0.5
tiempo_hablando_dalto=round(cantidad_palabras*0.35,2)
print("                 ")
print("Información frase ingresada")
print("-------------------------------------------------------------")
if tiempo_hablando>60:
    print("Para flaco tampoco te pedí un testamento")
else:
    print(f"Usted se tardaría aproximadamente {tiempo_hablando} segundos en decir la frase que ingresó.")
print(f"Dalto demoraría {tiempo_hablando_dalto} segundos en decir lo mismo que dijiste tú.")
print(f"La frase ingresada contiene {cantidad_palabras} palabras.")
print("--------------------------------------------------------------")