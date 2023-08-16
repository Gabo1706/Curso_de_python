#Realizar una función que entregue la sucesión de Fibonachi entre un rango dado
def fibonachi(limite_inferior,limite_superior):
    serie=[limite_inferior]
    while serie[-1]<limite_superior:
        if len(serie)==1:
            serie.append(serie[0]+serie[0])
        else:
            serie.append(serie[-1]+serie[-2])
            if serie[-1]>limite_superior:
                serie.pop()
                break
            else:
                continue
    return serie
limite_inferior=input(f"Ingrese el límite inferior de la serie de fibonachi: ")
limite_superior=input(f"Ingrese el límite superior de la serie de fibonachi: ")
print(fibonachi(int(limite_inferior),int(limite_superior)))