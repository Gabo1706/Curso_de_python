#Crear conjunto con función set, se ingresa una lista
conjunto=set(["Gabriel","González"])


#Metiendo un conjunto dentro de otro conjunto
#Un conjunto no se puede meter directamente a otro ya que esto arroja un error
#Es necesario hacer uso del método frozenset
conjunto1={"Gabriel","González"}
#conjunto2={conjunto1,"edad"}, esto arroja error porque no se puede
conjunto2={frozenset(conjunto1),"edad"}


#Teoría de conjuntos (basicamente subconjuntos y superconjuntos)
conjunto1={1,2,3,4,5}
conjunto2={1,3,5}

#Verificación de subconjunto
resultado=conjunto2.issubset(conjunto1) #usando método issubset
resultado=conjunto2<=conjunto1 #usando relación menor que


#Verificación de superconjunto
resultado=conjunto1.issuperset(conjunto2) #usando método issuperset
resultado=conjunto1>=conjunto2 #usando relación mayor que


