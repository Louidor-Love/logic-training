#chatbot analizador d sentimientos
#desarrolla un chatbot que nos pida que le digamos algo y 
#tome eso q le decimos,analice el sentimiento y ns respnda cual es el sentimiento

nombre = input("ingresee tu nombre: ")
palabra_input = input("Ingrese tus palabras: ")

class Usuario:
    def __init__(self, palabra_input, nombre):
        self.nombre = nombre
        self.palabra_input = palabra_input

    def __str__(self):
        return f"nombre de usuario {self.nombre}"   


class chatbot(Usuario):
    def __init__(self,palabra_input, nombre):
        super().__init__(palabra_input, nombre)
        self.palabra_input = palabra_input
        self.nombre = nombre

    def saludar(self):
        return f"buenos dias {self.nombre} espero q tuviste un buen dia"    
    def inicio(self):
        return "Ahora vamos a necesitar q ingreses algo,lo q sea,nosotros nos en cargamos d decirte cual es el sentimiento "  
    
    def analizar():
        pass

    def responder():
        pass

nombre = Usuario(palabra_input, nombre)
nombre = nombre.nombre    

print(chatbot(palabra_input,nombre).saludar())
print(chatbot(palabra_input,nombre).inicio())