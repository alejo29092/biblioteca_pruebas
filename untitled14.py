# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:42:47 2023

@author: alejo
"""

import pickle
from libro import Libro
class ListadeLibros:
    librosGuardados= []
    
    def __init__(self):
        archivoLibros = open("C:/Users/alejo/Desktop/poo/biblioteca/biblioteca_libros", "ab+")
        archivoLibros.seek(0)
        
        try:
           self.librosGuardados = pickle.load(archivoLibros)
           print(f"{len(self.librosGuardados)} libros guardados ")
        except EOFError:
            print("no se han cargado libros previos")
        finally:
            archivoLibros.close
            del archivoLibros
            
    def GuardarLibros(self):
        archivo = open("C:/Users/alejo/Desktop/poo/biblioteca/biblioteca_libros", "ab")
        pickle.dump(self.librosGuardados, archivo)
        archivo.close
        del archivo
        
            
        
    def agregarLibro(self,e):
        self.librosGuardados.append(e)
        self.GuardarLibros()
    
    def MostrarLibroGuardado(self):
        for e in self.librosGuardados:
           print(e)
           
libro1 = Libro('GAbriel', 'cien años de soledad', 'Colombia')
librosAgregar = ListadeLibros()
librosAgregar.agregarLibro(libro1)