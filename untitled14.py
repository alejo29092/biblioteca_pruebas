# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:42:47 2023

@author: alejo
"""

class ListadeLibros:
    librosGuardados= []
    
    def __init__(self):
        archivoLibros = open("C:/Users/alejo/Desktop/poo/biblioteca/biblioteca_libros", "ab+")
        archivoLibros.seek(0)
        
        self
        
        
        
        
    def agregarLibro(self,e):
        self.librosGuardados.append(e)
    
    def MostrarLibroGuardado(self):
        for e in self.librosGuardados:
           print(e)
           



lista1= ListadeLibros()
lista1.MostrarLibroGuardado()
