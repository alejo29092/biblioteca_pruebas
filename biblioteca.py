# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:40:14 2023

@author: alejo
"""


from libro import Libro
from Prestamo import Prestamos
from Estudiante import Estudiante



class Biblioteca():
    _seq_Biblioteca = 0
   
    
    def __init__(self, libro:Libro,nombre:str, prestamo:Prestamos):
        self._id = self._seq_Biblioteca
        Biblioteca._seq_Biblioteca +=1
        
        self._libro = (libro)
        self._nombre = (nombre)
    

    

    
def menu():
    seleccionar = 0
    while seleccionar !=7:
        print('Bienvenido al menú de la biblioteca')
        print('Primera versión 1.0')
        print('Elige una de las opciones')
        print('-----------------------------------------')
        print('1.) Registar un libro')
        print('2.) Registar un estudiante')
        print('3.) Buscar un libro ')
        print('4.) Buscar un estudiante')
        print('5.) Bucar un autor')
        print('6.) Mostrar libros')
        print('7.) Salir')
        seleccionar= int(input('Elige una opcion: '))
        if seleccionar ==1:
            RegistarLibro()
        elif seleccionar ==2:
            RegistarEstudiante()
        elif seleccionar == 3:
            BuscarLibro()
        elif seleccionar == 4:
            BuscarEstudiante()
        elif seleccionar == 5:
            BuscarAutor()
        elif seleccionar == 6:
            MostrarLibro()
        print('---------------------------------------')
LibrosPosesion = list()
LibrosPrestamo = list()

def RegistarLibro():
    libros = Libro
    libros.autor = input('introduce el autor: ')
    libros.nombre=input('introduce el nombre del libro: ')
    libros.pais=input('introduce el pais de origen del libro: ')
  
    LibrosPosesion.append(libros)
   
def RegistarEstudiante():
    estudiantes = Estudiante()
    estudiantes.nombre = input('introduce el nombre del estudiante')
    
def BuscarLibro():
    id_libro = int(input('ingresar id del libro a buscar'))
    for libros in LibrosPosesion:
        if libros._id == id_libro:
            print(libros.nombre,',', ',',libros.autor,',', libros.pais)

def BuscarEstudiante():
    print('f')
def BuscarAutor():
    print('K')
def MostrarLibro():
    for libros in LibrosPosesion:
       print('el libro',libros.nombre,' de Autor ', libros.autor, ' y fue echo en ', libros.pais)
           
    
menu()
        
        
        
