# Tenés una función "aplicar_a_lista"
# que recibe:
# - una función (func)
# - una lista de números
# 
# Debe devolver una nueva lista con la función aplicada a cada elemento

def aplicar_a_lista(func, lista):
    resultado = []
    for i in lista:
        resultado.append(func(i))
    
    return resultado



    
print("resultado")
resultado = aplicar_a_lista(lambda x:  x*2, [1,2,3,4])    
print(resultado)