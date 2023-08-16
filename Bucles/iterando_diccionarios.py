diccionario={
    'nombre': 'gabriel',
    'apellido': 'gonzalez',
    'edad': 18}

#para recorrer el diccionario se usa el método items que devuelve una tupla conteniendo en la primera posición la clave y en la segunda posición el valor

for datos in diccionario.items():
    claves=datos[0]
    valores=datos[1]
    print(f"la clave es {claves}")
    print(f"y su valor es {valores}")

#nota: si intenta recorrer el diccionario solo sin método solo va devolver las claves, no devuelve los valores de dichas claves
