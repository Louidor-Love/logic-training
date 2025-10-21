#chatbot analizador d sentimientos
#desarrolla un chatbot que nos pida que le digamos algo y 
#tome eso q le decimos,analice el sentimiento y ns respnda cual es el sentimiento

palabra_input = input("Ingrese algo: ")

class Usuario:
    def __init__(self, palabra_input):
        self.palabra_input = palabra_input


usuario = Usuario(palabra_input)

class chatbot:
    def __init__(self,usuario):
        self.usuario = usuario

