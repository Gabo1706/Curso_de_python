#len indica la cantidad de elementos que tiene la lista
a=["asdsa","sdsdfd",323,23,432]
b=len(a)

#append agrega elementos al final de la lista (a la lista original)
a=["asdsa","sdsdfd",323,23,432]
a.append("Hola rey")
print(a)
#insert agrega un elemento en un pindice específico a la lista, el primer parámetro indica el indice y el otro indica lo que se quiere agregar

a=["asdsa","sdsdfd",323,23,432]
a.insert(1,"esto se acaba de insertar")

#extend agrega una lista a una lista (el parámetro dentro de los paréntesis debe ser una lista)
a=["asdsa","sdsdfd",323,23,432]
a.extend(["assd",True,23])

#pop elimina el elemento de un indice específico (el parametro adentro debe indicar el índice que se quiere borrar)
#el indice también puede ser negativo, al ser negativo va de atrás para adelante
#es decir -1 es el último elemento, -2 es el penultimo y así sucesivamente
a=["asdsa","sdsdfd",323,23,432]
a.pop(1)


#remove quita un elemento específico de lista pero por su valor
a=["asdsa","sdsdfd",323,23,432]
a.remove(23)


#clear elimina todos los elementos de la lista
a=["asdsa","sdsdfd",323,23,432]
a.clear()

#sort ordena los elementos de menor a mayor (deben ser datos numéricos)
#para hacerlo de mayor a menor se pone reverse=True adentro de los paréntesis del método
a=[123,4324,53,132,423,4]
b=[123,4324,53,132,423,4]
a.sort()
b.sort(reverse=True)


#reverse voltea toda la lista sin importar que tipo de datos sea
a=[123,4324,53,132,423,4]
a.reverse()


