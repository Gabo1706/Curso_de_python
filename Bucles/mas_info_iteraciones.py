#CONTINUE: este se usa para que salte de iteración y pase a la siguiente
frutas=["manzana","pera", "mora","durazno","papaya"]
for fruta in frutas:
    if fruta=="mora":#estamos saltando la fruta mora con la sentencia CONTINUE
        continue
    print(f"me voy a comer una {fruta}")
    
#BREAK rompe el ciclo y lo termina

for fruta in frutas:
    if fruta=="durazno":
        break
    print(f"esta es la nueva fruta que me voy a comer: {fruta}")