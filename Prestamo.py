
"""
Created on Mon Feb 20 12:40:47 2023

@author: alejo
"""


from libro import Libro
from Estudiante import Estudiante

class Prestamos:
    
    def __init__(self, libro:Libro, estudiante:Estudiante):
            LibrosPrestamo = list()
            self._libro =libro
            self._estudiante = estudiante
            LibrosPrestamo.append(self)
        
    def getEstudiante (self):
             return self.estudiante
         
    def getDeudaEstudiante (self):
             return self._estudiante
             return self._libro
      
        
        
