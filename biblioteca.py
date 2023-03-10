# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:40:14 2023

@author: alejo
"""

from libro import Libro
from libro import ListaDeLibros
from Prestamo import Prestamos
from Estudiante import Estudiante
from libro import RegistarLibro


class Biblioteca():
    """
    Esta 
    """
    _seq_Biblioteca = 0
   
    
    def __init__(self, libro:Libro,nombre:str, prestamo:Prestamos):
        self._id = self._seq_Biblioteca
        Biblioteca._seq_Biblioteca +=1
        
        self._libro = (libro)
        self._nombre = (nombre)
        #self._repositorio = RegistrarLibro
    

LlamarLibro = ListaDeLibros()
def menu():
    """
    da un menu de opciones y sus respectivors numeros para
    ser usada
    """
    seleccionar = 0
    while seleccionar !=7:
        
        print('Bienvenido al menú de la biblioteca')
        print('Primera versión 1.0')
        print('Elige una de las opciones')
        print('-----------------------------------------')
        print('1.) Registar un libro')
        print('2.) Registar un estudiante')
        print('3.) Buscar un libro por su id')
        print('4.) Buscar un estudiante')
        print('5.) Bucar un autor')
        print('6.) Mostrar libros')
        print('7.) Salir')
        seleccionar= int(input('Elige una opcion: '))
        if seleccionar ==1:
            LlamarLibro.RegistrarLibro()
        elif seleccionar ==2:
            RegistarEstudiante()
        elif seleccionar == 3: 
            LlamarLibro.BuscarLibroId()
        elif seleccionar == 4:
            BuscarEstudiante()
        elif seleccionar == 5:
            BuscarAutor()
        elif seleccionar == 6:
            MostrarLibros()
        print('---------------------------------------')

libros = Libro

    
def RegistarEstudiante():
    estudiantes = Estudiante()
    estudiantes.nombre = input('introduce el nombre del estudiante')
    
    

            
def BuscarEstudiante():
    print('x')
        
def BuscarAutor():
    id_libro = int(input('ingresar id del libro a buscar'))
    for ibros in listas :
        if libros.autor == id_libro:
            print(libros.nombre,',', ',',libros.autor,',', libros.pais)
        
        
def MostrarLibros():
    print(ListaDeLibros.MostrarLibroGuardado())

  


menu()
        
        
        
