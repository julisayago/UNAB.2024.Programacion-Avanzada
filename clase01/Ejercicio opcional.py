#Seleccionar 2 (dos) de los pilares (o pilares asociados) y arme un breve resumen con:
#Breve explicación con sus palabras
#Programar un ejemplo en Python y explicar cómo aplica este concepto

#ABSTRACCIÓN: cuando se habla de una clase, es la acción de nombrar y definir sus métodos y atributos.
#HERENCIA: cuando una clase (hijo) hereda los atributos y métodos de la clase superior (padre).
 
class Transporte ():

    def __init__(self, ruedas, velocidad, pasajeros):
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.pasajeros = pasajeros

    def cantidad_ruedas (self):
        return "Este transporte tiene " + str(self.ruedas) + " ruedas"
    
    def mover (self):
        return "Este transporte se desplaza a " + str(self.velocidad) + " km por hora"

    def cantidad_pasajeros (self):
        return "Este transporte puede llevar hasta " + str(self.pasajeros) + " pasajeros"
    
class Auto (Transporte):

    def __init__(self, ruedas, velocidad, pasajeros, marca, modelo):
        super().__init__(ruedas, velocidad, pasajeros)
        self.marca = marca
        self.modelo = modelo

    def informacion_auto (self):
        return "Este auto es marca " + str(self.marca) + " y es el modelo " + str(self.modelo)
    
class Avión (Transporte):

    def __init__(self, ruedas, velocidad, pasajeros, aerolinea):
        super().__init__(ruedas, velocidad, pasajeros)
        self.aerolinea = aerolinea

    def despegar (self):
        return "El avión está despegando"
    
    def informacion_avion (self):
        return "El avión pertenece a la aerolinea " + str(self.aerolinea)
    
mi_auto = Auto (4, 120, 5, "Renault", "Clio")
mi_avion = Avión (22, 889, 500, "Qatar Airways")

print(mi_auto.cantidad_ruedas())
print(mi_auto.mover())
print(mi_auto.cantidad_pasajeros())
print(mi_auto.informacion_auto())

print(mi_avion.cantidad_ruedas())
print(mi_avion.mover())
print(mi_avion.despegar())
print(mi_avion.informacion_avion())
