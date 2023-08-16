#estas funciones son cuando la operación es corta
multiplicar_por_dos=lambda x: x*2
#print(multiplicar_por_dos(3))

#ejemplo con función filter: esta función solo muestra los parametros True
numeros=[4,3,2,4,5,5,4,32]
numeros_pares= filter(lambda numero: numero%2==0,numeros)
print(list(numeros_pares))