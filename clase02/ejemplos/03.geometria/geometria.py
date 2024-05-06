class Figura:
    pass

class Poligono(Figura):
    def __init__(self, *lados):
        self.lados = lados

    def perimetro(self):
        return sum(self.lados) * 2

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__(lado, lado)

class Rectangulo(Poligono):
    def __init__(self, lado1, lado2):
        super().__init__(lado1, lado2)

#TODO: Pensar en otra posible herencia (taxonomía) -> Ambas pueden clasificarse dentro de la clase poligonos ✅

c1 = Cuadrado(6)
c2 = Cuadrado(4)
print(c1.perimetro())  
print(c2.perimetro())

r1 = Rectangulo(3, 4)
r2 = Rectangulo(4, 10)
print(r1.perimetro()) 
print(r2.perimetro())  