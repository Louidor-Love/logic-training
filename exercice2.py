milan = {"kaka":11, "pato":9, "ibrahimovic": 10, "seedorf": 6, "malidini": 3, "nesta":5}

for nombre,numero in milan.items():
    if nombre == "kaka":
        print(f"el numero siempre va ser {numero}")
    print(f"pero el nombre y numero del equipo en general es {nombre} - {numero}")        

for nombre in milan:
    print(nombre)

num = milan ["kaka"] 
print(num)