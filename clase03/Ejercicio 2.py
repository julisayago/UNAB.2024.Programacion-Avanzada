#Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente constructor que recibe ambos valores.
#Definir métodos tales como: eje_x, eje_y , impresion (método que devuelve en representación de string ambos valores), opuesto (método que devuelve el punto opuesto -es decir con los atributos negativos-) o ualquier otro método que considere importante

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        print("(" + str(self.x) + "," + str(self.y) + ")")

    def opuesto(self):
        print("(-" + str(self.x) + ",-" + str(self.y) + ")")

punto1 = Punto(3, 4)
punto2 = Punto(2, 7)
print("Coordenada x de punto1:", punto1.eje_x())
print("Coordenada y de punto1:", punto1.eje_y())
punto1.impresion()
punto2.opuesto()

