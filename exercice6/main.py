import pandas as pd

datos = {
    "Nombre": ["An,a", "Car,los", "Sofía"],
    "Edad": [25, 30, 22],
    "País": ["Argentina", "México", "Colombia"]
}

df = pd.DataFrame(datos)
#print(pd)

df[["Nombre1", "Nombre2"]] = df["Nombre"].str.split(",", expand=True)

print(df.columns)

#valor y clave
for index,row in df.iterrows():
    print(f"la fila es  : {index} -el valor d Nombre es : {row['Nombre']} -el valor d edad es  :{row['Edad']}")
    

#las columnas
print(df.columns)
#cierta columna 
print(df[["Nombre","Edad"]]) 
#itrar sobre las columnas  
print(df[["Nombre","Edad"]].values) 
df_filtrado = df [["Nombre","Edad"]]
for i in df_filtrado:
    if i == "Nombre":
        print(f"las columnas presentes son {i}")

#iterar sobre los valores d las columnas
df_filtrado1 = df [["Nombre","Edad"]].values

for i in df_filtrado1:
    print(f"los valores d las columnas son {i} ")

print(df[["Nombre","Edad"]])     
  