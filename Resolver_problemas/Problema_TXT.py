#Se entregan dos listas, una con nombres y otra con apellidos, Escribir nombres y apellidos en forma de texto con un for
nombres=["Hernán","Gisell","Juan","Miguel","Silvana","Gabriel"]
apellidos=["González","Ramírez","Carrillo","Álvarez","Pérez","Sarmiento"]

with open("Resolver_problemas\\Nombres y apellidos.txt","w",encoding="UTF-8") as doc:
    
    for nombre,apellido in zip(nombres,apellidos):
        doc.writelines(f"{nombre} {apellido}\n")
        
#El código anterior está correcto, sin embargo, se puede expresar en una sola línea como se muestra a continuación

with open("Resolver_problemas\\Nombres y apellidos.txt","w",encoding="UTF-8") as doc:
    [doc.writelines(f"{nombre} {apellido} \n") for nombre,apellido in zip(nombres,apellidos)]
    
#En este caso el for se puso después del .writelines
#como se puede notar no hay problema con llamar las variables nombre y apellido con tal de que en la misma línea se creen.
    