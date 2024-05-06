#Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que pasa la línea en un espacio de dos dimensiones.

#La clase dispondrá de los siguientes métodos:
#Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase Punto, que son utilizados para inicializar los atributos.
#mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
#mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
#mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
#mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Linea:
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b

    def mueve_derecha(self, distancia):
        self.punto_a.x += distancia
        self.punto_b.x += distancia

    def mueve_izquierda(self, distancia):
        self.punto_a.x -= distancia
        self.punto_b.x -= distancia

    def mueve_arriba(self, distancia):
        self.punto_a.y += distancia
        self.punto_b.y += distancia

    def mueve_abajo(self, distancia):
        self.punto_a.y -= distancia
        self.punto_b.y -= distancia