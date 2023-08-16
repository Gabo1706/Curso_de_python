# dir: devuelve los métodos aplicables al objeto en estudio [Función de python, por eso entre paréntesis]
a=dir("Hola")

#UPPER convierte todo a mayúscula [al ser método se hace con un punto]
#ESTRUCTURA DE UN MÉTODO --> DATO.METODO()

a="Hola como estás"
b=a.upper()

#LOWER convierte todo a minúscula

a="HOLA COMO ESTAS"
b=a.lower()

#CAPITALIZE convierte todo en minúscula y luego convierte la primera letra en mayúscula

a="hola como tas"
b=a.capitalize()

#FIND busca una cadena en otra cadena, muestra la posición en la que está la cadena encontrada, en caso de no encontrarla retorna -1
a="Hola como tas"
b=a.find("tes")

#index hace lo mismo que FIND pero en caso de no encontrar nada bota error


#isnumeric indica si el string es netamente numérico a pesar de ser un string

a="3928402"
b=a.isnumeric()


#count indica cuantas veces ocurre una coincidencia en una cadena dada si no hay councidencia devuelve 0

a="Hola, como esta ella"
b=a.count("bksdbsdkc")

#len cuenta la cantidad de caracteres, esta es una función no un método

a="Hola como tas"
b=len(a)

#startswith verifica si la cadena empieza por otra cadena dada
b=a.startswith("Hla")

#endswith verifica si la cadena termina por otra cadena dada
b=a.endswith("s")

#replace reemplazaa un pedazo de la cadena con otra cadena. si no encuentra la cadena que se quiere reemplazar no se realiza ningún reemplazo
#la sintaxis es que primero se pone lo que se quiere reemplazar y luego con que se va reemplazar
#OBJETO.REPLACE("ANTIGUO","NUEVO")
b=a.replace("hola","Holi")


#split devuelve una lista de cadenas separadas por una cadena dada  

a="Hola,Como,estás,mi,rey"
b=a.split(",")
print(b)