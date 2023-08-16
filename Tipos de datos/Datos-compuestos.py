#listas 
# se permiten editar, son un arreglo que agrupa datos y se definen con []
#poseen indexación
lista=["Gabriel Gonzalez","Estudiante",180,21]
lista[3]=24


#Tuplas
#Lo mismo de las listas pero no se pueden editar, se definen con ()

tupla=("Gabriel Gonzalez","Estudiante",180,21)

#Conjuntos (no se pueden alterar ni repetir datos) almacena datos pero sin un orden especifco de modo que no tiene indexación

conjunto={"Gabriel Gonzalez","Estudiante",180,21,21,21}

#diccionario
#lo mismo que la lista pero se define el indice con palabras key : value y se separa con comas cada elemento
diccionario={
    'Nombre': 'Gabriel González',
    'Ocupación' : 'Estudiante',
    'altura' : 180,
    'edad' : 21
    }

print(diccionario['Ocupación'])

