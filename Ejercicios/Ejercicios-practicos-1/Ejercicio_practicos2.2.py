#Crear una función que reciba un número y entregue todo los números primos hasta ese número
def encontrar_primos(numero_tope):
    lista_respuesta=[]
    for i in range(2,int(numero_tope)+1):
        if i==2:
                lista_respuesta.append(i)
        else:
            for primo in lista_respuesta:
                marcador=True
                if i%primo==0:
                    marcador=False
                    break
                else:
                    continue
            if marcador==False:
                continue
            else:
                lista_respuesta.append(i)
    return lista_respuesta
numero_tope=input(f"Ingrese hasta que número saber que números primos hay: ")
print(encontrar_primos(numero_tope))
