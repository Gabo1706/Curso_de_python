#Los módulos son todos los archivos .py
#Esto significa que se puede hacer uso de cualquier código en otro archivo siempre y cuando se importe en el archivo en elque se está trabajando
#Para hacer eso se debe hacer uso de la función import
#SINTAXIS
#Se pone al inicio del doc asi: import nombre_del_archivo
#Una vez importado las funciones contenidas en el archivo se comportarán como métodos u objetos
#Ejemplo: Tengo una función llamada Fibonachi entonces para usarla se hace: nombre_del_modulo.funcióndedichomodulo()
def saludo(nombre):
    return f"Hola {nombre}, como estás el día de hoy."
