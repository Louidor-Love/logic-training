ingrediente = {"harina":"trigo", 
              "condimento":["perejil","oregano","pimenton"],
              "verdura": ["cebolla", "ajo","aji"],
              "queso": "mozarella"}



for clave ,valor in ingrediente.items():
    for i in valor:
        print(f"los valores son: {i}")
    for c in clave:
        print(f"las claves son: {c}")    
   