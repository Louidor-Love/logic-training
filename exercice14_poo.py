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
        return f" nombre de usuario {self.nombre}"   


usuario = Usuario(palabra_input)
nombre = Usuario(palabra_input)


class chatbot:
    def __init__(self,usuario,nombre):
        self.usuario = usuario
        self.nombre = nombre

    def saludar(self):
        return f"buenos dias {self.nombre} espero q tuviste un buen dia"    

