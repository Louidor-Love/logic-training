import pandas as pd

datos = {
    "Nombre": ["Ana", "Carlos", "Sofía"],
    "Edad": [25, 30, 22],
    "País": ["Argentina", "México", "Colombia"]
}

pd = pd.DataFrame(datos)
#print(pd)

for index,row in pd.iterrows():
    print(f"la clave es  : {index} -el valor es : {row['Nombre']}")