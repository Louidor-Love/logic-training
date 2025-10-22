# crear un sistema para una escuela ...el sistema va tener 2 clases principales: Persona y Estudiante
# la clase Persona tendra los atributos d nombre y edad y un metdod q imprima el nmbre y edad d la persona
#la clase estudiante heredara d la clase Persona y tmb tendra un atributo adicional : grado y un metdo
# q imprima el grado del estudiante

nombre = (input("ingreses el nmbre:"))
edad = int(input("ingreses la edad:"))
grado = int(input("ingreses la edad:"))
class Persona:
    def __init__ (self,nombre ,edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_persona(self):
        print( f"edad :{self.edad} - nombre:{self.nombre}")    

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado) :
        super().__init__(nombre, edad)
        self.grado = grado

    def imprimir_persona(self):
        return super().imprimir_persona()   

    def imprimir_estudiante(self):
        print( f"grado :{self.grado}" )    

estudiante = Estudiante(nombre,edad,grado)
estudiante.imprimir_persona()
estudiante.imprimir_estudiante()