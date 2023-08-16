#Para crear una función se usa la siguiente sintaxis
#def NOMBRE_DE_LA_FUNCION(PARAMETROS,DE,LA,FUNCION)
#la función acaba con return lo cual permite almacenar la salida de la función
#en este caso los argumentos están organizacionalmente ordenados, es decir por el orden en que se le ingresen se van a acomodar los parámetros
def saludo(nombre,sexo):
    sexo=sexo.lower()
    if sexo=="mujer":
        adj="reina"
    else:
        adj="Rey"
    return f"Hola {nombre} mi {adj} como vamos?" 
    
saludo_general=saludo("Gabriela","mujer")

    
    
#parametro *args
#este asterísco lo que hace es que vuelve un conjunto de parámetros en uno solo para meterlo en la función
def suma_args(*numeros):
    return sum([*numeros]) #se mete en una lista para usar la funcion interna sum
#print(suma_args(2,3,4,5,6,2)) #acá no importa la cantidad de números se ponga en el parámetro
#si no se hiciera con *args la cantidad de argumentos metidos si importa

#funciones con parametros fijos a la "fuerza"
#acá en vez de ser organizados por el orden se organizan asignandole el nombre directamente
def saludo2(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"
mostrar1=saludo2("Gabriel","González","alto")#acá los parámteros están organizacionalmente
mostrar2=saludo2(apellido="González", adjetivo="alto", nombre="Gabriel")#acá se asignaron directamente los parámetros
#print(mostrar1)
#print(mostrar2)
#Los resultados anteriores son iguales porque están haciendo lo mismo 