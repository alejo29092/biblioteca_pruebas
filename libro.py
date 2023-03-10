import pickle


class Libro:
    
    GuardadosId = [1000]
    _seq_Libro = 1000
    Ruta = "biblioteca_id"

    def __init__(self, nombre: str, pais: str, estado:False):
        """
        Crea un libro en donde se crean las siguientes variables
        _nombre : es el nombre del libro.
        _pais: el pais de origen del libro.
        _autor: aqui se le da un autor al libro, y en caso de no exirtir 
        un autor, se crea uno nuevo.
        ademas se pone en minuscula todos ellos
        por otro lado se mantiene la id
        
        """
        
        
        
        self._nombre = nombre.lower()
        self._pais = pais.lower()
        self._estado = estado
        
        
        ArchivoId = open( self.Ruta, "ab+")
        ArchivoId.seek(0)
        try:
             self._seq_Libro = pickle.load(ArchivoId)
             
        finally:
            del self._seq_Libro
        
        Libro._seq_Libro += 1
        self._id = self._seq_Libro 
        Archivo = open(self.Ruta, "ab")
        pickle.dump(self._seq_Libro, Archivo)
        Archivo.close
        del Archivo  
        
    
    def __str__(self):
        return f"{ self._nombre}, {self._pais}, {self._autor}, {self._id}, {self._estado}"
  




 
       
      
