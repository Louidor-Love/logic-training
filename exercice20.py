
text = """
Creo que a veces es la gente de la que nadie espera nada,
la que hace cosas que nadie puede imaginar.
Pero a veces, la gente cambia... y nadie lo nota.
"""

def analyze_text(text: str) -> dict:
    text1 = text.split()
    # contar palabras
    word_count = {}
    for palabra in text1:
        clean_word  = palabra.lower().strip(",/.?!;:()\"'") 
        if clean_word  not in word_count:
            word_count[clean_word] = 1
        else:
            word_count[clean_word] += 1

        # Convertimos el diccionario a lista de tuplas y ordenamos por frecuencia
        world_count = list(word_count.items())
        world_count.sort(key=lambda x: x[1], reverse=True)
        # 3. Nos quedamos con las primeras 3 palabras
        top_3 = [word for word, count in world_count[:3]]
   
    return world_count , top_3

world_count, top_3 = analyze_text(text)

print(f"mi top 3 mas frecuentes: {top_3}")
print(f"conteo de palabras: {world_count}")
