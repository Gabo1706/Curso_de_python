diccionario={
    'nombre': 'Gabriel',
    'apellido': 'Gonzalez',
    'edad': 20,
    'estatura':180
}

#keys devuelve las llaves del diccionario (también sirve para iterar)
a=diccionario.keys()

#get muestra el valor de una llave en específico
a=diccionario.get('edad') #debe retornar Gonzalez

#clear borra todo del diccionario

#pop elimina un elemento del diccionario
diccionario.pop('nombre')

