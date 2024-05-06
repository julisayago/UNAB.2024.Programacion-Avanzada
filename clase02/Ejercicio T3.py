#En base a un ejemplo que plantee el uso de dos clases con la relación “es un” definir:
#Nombre de cada clase
#Propiedades (al menos 2 por cada clase)
#Métodos (al menos 2 por cada clase)
#Instanciación de Objetos (al menos 2 objetos por cada clase)

class Animal:
    def __init__(self, edad, peso) -> None:
        self.edad = edad 
        self.peso = peso 
    
    def edad_animal (self):
        return "El animal tiene " + str(self.edad_animal) + "años"
    
    def peso_animal (self):
        return "El animal pesa " + str(self.peso_animal)
    
class Perro (Animal):
    def __init__(self, edad, peso, raza) -> None:
        super().__init__(edad, peso)
        self.raza = raza

    def obtener_raza (self):
        return "El perro es de la raza " + self.raza
    
    def ladrar (self):
        return "Guau!"
    
animal1 = Animal(5, 25)
animal2 = Animal(3, 15)

perro1 = Perro(4, 20, "Labrador")
perro2 = Perro(6, 18, "Bulldog")

#Elaborar conclusiones incluyendo opiniones sobre:
#Grado de dificultad del ejercicio (escala de 1 a 5): 3, me resultó difícil identificar métodos y atributos específicos para la clase Perro.
#¿Qué tema le resultó de mayor dificultad?: Encontrar métodos y atributos para la clase Perro, sin que estos sean compartidos por las instancias de Animal.
#¿Cómo resolvería esta ejercitación si tuviera de repetirla? ¿Qué cambiaría?: Consideraría elegir otro tema o animal para evitar la complejidad de diferenciar entre las características de los perros y las compartidas por todos los animales. También podría replantear el diseño de las clases para hacerlo más claro y fácil de entender.