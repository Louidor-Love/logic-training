# en la variable 'text' dispones de una cadena de texto
# debes contar las palabras y devolver cuantas veces se repiten cada una de ellas
# ejemplo --> 'nadie' aparece 2 veces

text = "creo que a veces es la gente de la que nadie espera nada ,la que hace cosas que nadie puede imaginar"

text1 = text.split()
for palabra in text1:
    print(f"la palabra - [{palabra}] se repitio - [{text1.count(palabra)}] veces ")


   