list = ["lucio","julius",1,1,2,"lucio",3,4,5,2,2]
list_sin_duplicar = []
duplicados = []

for i in range  (len(list)):
    duplicado_encontrado = False
    for y in range (i+1, len(list)):
        if list[i] == list[y]:
            duplicado_encontrado = True

    # recién después de revisar todos
    if duplicado_encontrado:
        # evita repetir duplicados
        if list[i] not in duplicados:
            duplicados.append(list[i])
    else:
        # evita repetir duplicados   
        if list[i] not in list_sin_duplicar:
            list_sin_duplicar.append(list[i])
            

            
      

duplicados.append(list[y])
list_sin_duplicar.append(list[y]) 

print(f"la lista sin duplicar es: \n {list_sin_duplicar}")
print(f"los duplicados son: \n {duplicados}")
