# Escribe un código que cuente cuántas frutas hay en la categoría "rojas" e imprima el resultado en este formato:
# print("Número de frutas rojas:", cantidad)

print("ejercicio 1")
frutas = {
    "rojas": ["manzana", "cereza", "fresa"],
    "amarillas": ["plátano", "piña", "limón"],
    "verdes": ["pera", "uva", "kiwi"]
}

for clave,valor in frutas.items():
    if clave == "rojas":
        print(f"Número de frutas rojas:, {len(valor)}")


#Buscar un elemento dentro de una lista en un diccionario
#Escribe un código que pregunte al usuario un nombre y luego verifique si ese nombre está en la lista del "curso2". 
#Si está, imprime "El estudiante está en curso2", si no, imprime "El estudiante no está en curso2".

print("ejrcicio2")

alumnos = {
    "curso1": ["Ana", "Carlos", "Pedro"],
    "curso2": ["María", "Javier", "Lucía"],
    "curso3": ["Fernando", "Sofía", "Martín"]
}
nombre = input("Ingrese un nombre: ")


def verifique(nombre,alumnos):
    if nombre in alumnos["curso2"]:
        print("existe")
    else:
        print("no existe")     

verifique(nombre,alumnos)     

#Agregar elementos a una lista dentro de un diccionario
#Escribe un código que agregue "Manchester United" a la lista de "fútbol" e imprima el diccionario actualizado.

print("ejercicio3")

equipos = {
    "fútbol": ["Real Madrid", "Barcelona", "Juventus"],
    "baloncesto": ["Lakers", "Chicago Bulls", "Miami Heat"],
    "tenis": ["Federer", "Nadal", "Djokovic"]
}


equipos["fútbol"].append("Manchester United")
print(equipos)


