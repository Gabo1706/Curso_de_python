#CICLO FOR 
#Crea una variable que recorre el elemento
#SINTAXIS for VARIABLE_NUEVA  in VARIABLE_A_RECORRER:
animales=["perro","gato","conejo","serpiente"]
for animal in animales:
    print(f"la variable animales va en {animal}")
    
    
#iterar varias listas del mismo tamaño usando zip
lista1=[11,22,33,44,55]
for numero,animal in zip(lista1,animales):
    print(f"la variable animales va en {animal}")
    print(f"la variable numero va en {numero}")
    
#recorrer con enumerate: enumerate agarra la lista y devuelve una tupla que en su primera posición ínidca el índice del valor y en la segunda posición indica el valor
#es una forma eficiente de recorrer una lista extrayendo su índice    
for i,num in enumerate(lista1):
    print(f"este es el numero {num} ")
    print(f"este es el indice {i}")

