nombres =["monica", "patricia", "Karla", "mariela"]
print(nombres)
#f-strings
for i , nombre in enumerate(nombres):
    #print("se escribio", "en la lista:",i, nombre)
    print(f"se escribio {nombre} en la lista con indice {i}")

print("Bienvenidos a la fiesta", nombres[:3 ])
print("Lo sentimos", nombres [3:])
