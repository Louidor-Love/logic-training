import pandas as pd

datos = {
    "Nombre": ["Ana", "Carlos", "Sofía"],
    "Edad": [45, 30, 22],
    "País": ["Argentina", "Cuba", "Costarica"]
}

datos1 = {
    "Nombre": ["Julio", "Cesar", "Sofíana", "Joe", "Tatiana"],
    "Edad": [45, 60, 42, 34, 50],
    "País": ["Haiti", "Cuba", "Costarica","Argentina", "usa"]
}

df = pd.DataFrame(datos)
df1 = pd.DataFrame(datos1)
print("el primer df es:")
print(df)

print("el segundo df es:")
print(df1)

resultado = pd.merge(df, df1, on='País', how='inner', suffixes=('_df', '_df1'))
print('el cruce es: ')
print(resultado)
