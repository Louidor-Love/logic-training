import pandas as pd

datos = {
    "Nombre": ["Ana", "Carlos", "Sofía"],
    "Edad": [25, 30, 22],
    "País": ["Argentina", "México", "Colombia"]
}

df = pd.DataFrame(datos)
#print(pd)

for index,row in df.iterrows():
    print(f"la clave es  : {index} -el valor es : {row['Nombre']}")

#las columnas
print(df.columns)
#cierta columna 
print(df[["Nombre","Edad"]]) 
#itrar sobre las columnas  
print(df[["Nombre","Edad"]].values) 