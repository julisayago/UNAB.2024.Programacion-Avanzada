import math

def area_cuadrado(lado):
    return lado ** 2

def perimetro_cuadrado(lado):
    return lado * 4

lado = int(input("Ingrese la longitud del lado del cuadrado: "))
area = area_cuadrado(lado)
perimetro = perimetro_cuadrado(lado)

print("El área del cuadrado es", area)
print("El perímetro del cuadrado es", perimetro)

def area_rectangulo(lado1, lado2):
    return lado1 * lado2

def perimetro_rectangulo(lado1, lado2):
    return (lado1 * 2) + (lado2 * 2)

lado1 = int(input("Ingrese la longitud del primer lado del rectángulo: "))
lado2 = int(input("Ingrese la longitud del segundo lado del rectángulo: "))
area_r = area_rectangulo(lado1, lado2)
perimetro_r = perimetro_rectangulo(lado1, lado2)

print("El área del rectángulo es", area_r)
print("El perímetro del rectángulo es", perimetro_r)

def area_circulo(radio):
    return math.pi * radio ** 2

def perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
area_c = area_circulo(radio)
perimetro_c = perimetro_circulo(radio)

print("El área del círculo es", area_c)
print("El perímetro del círculo es", perimetro_c)