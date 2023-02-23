from autor import Autor


class Libro:
    _seq_Libro = 0
   

    def __init__(self, autor: Autor, nombre: str, pais: str):
        self._id = self._seq_Libro
        Libro.seq_Libro += 1
        
        self._nombre = nombre
        self._pais = pais
        self._autor = autor
        
        
    def getNombre (self):
        return self._nombre
    

    def getInfoLibro(self):
     return self._nombre
     return self._pais
     return self._autor
    def __str__(self):
        return (self._nombre, self._pais,self._autor)
  
 
 
     
 
 
       
      
