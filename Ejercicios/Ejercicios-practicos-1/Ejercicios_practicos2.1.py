#Ejercicio 1
#Pedir datos
estudiantes=[]
for indice in range(3):
    edad=input(f"Indique  la edad del estudiante {indice+1}: ")
    nombre=input(f"Indique el nombre del estudiante {indice+1}: ")
    estudiante=(nombre,edad)
    estudiantes.append(estudiante)
estudiantes.sort(key=lambda x:x[1])
print(f"{estudiantes[0][0]} es el profesor de la clase con {estudiantes[0][1]} años.")
print(f"{estudiantes[-1][0]} es el profesor de la clase con {estudiantes[-1][1]} años.")


    
