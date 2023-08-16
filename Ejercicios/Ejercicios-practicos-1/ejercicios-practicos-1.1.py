#punto a
duración_máxima=7
duración_promedio=4
duración_mínima=2.5
duracion_actual=1.5

diferencia_con_maximo=round(100-((duracion_actual*100)/duración_máxima),2)
diferencia_con_promedio=round(100-((duracion_actual*100)/duración_promedio),2)
diferencia_con_minima=round(100-((duracion_actual*100)/duración_mínima),2)



#punto b
material_crudo_promedio=5
material_crudo_actual=3.5

diferencia_material_promedio=round(100-((duración_promedio*100)/material_crudo_promedio),2)
diferencia_material_actual=round(100-((duracion_actual*100)/material_crudo_actual),2)


#punto c

porcentaje_de_maximo=round((duracion_actual*100)/duración_máxima,2)
porcentaje_de_promedio=round((duracion_actual*100)/duración_promedio,2)
porcentaje_de_minimo=round((duracion_actual*100)/duración_mínima,2)

equivalente_máximo=round((100*10)/porcentaje_de_maximo,2)
equivalente_promedio=round((100*10)/porcentaje_de_promedio,2)
equivalente_minimo=round((100*10)/porcentaje_de_minimo,2)

print(equivalente_minimo)
print(equivalente_promedio)
print(equivalente_máximo)