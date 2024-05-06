"""
Ejercicio 5:
● Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
(ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes
servicios: getters y setters, método para leer la información y método para mostrar la
información.
● Este último método mostrará la información del libro con este formato:
Título: Introduction to Java Programming 3a. edición
Autor: Liang, Y. Daniel
ISBN: 0-13-031997-X
Prentice-Hall, New Jersey (USA)
viernes 16 de noviembre de 2001
784 páginas
"""
class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

class Libro:
    def __init__(self, titulo, autor, ISBN, paginas, edicion, editorial, lugar, fecha_edicion) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion

    def mostrar_informacion (self):
        print ("Título:", self.titulo, self.edicion)
        print ("Autor:", self.autor.nombre, self.autor.apellido)
        print ("ISBN:", self.ISBN)
        print(self.editorial, self.lugar)
        print(self.fecha_edicion)
        print(self.paginas, "páginas")
