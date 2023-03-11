import pickle
from autor import Autor


class Libro:
    _seq_Libro = 1000

    def __init__(self, nombre: str, pais: str, autor: Autor):
        """
        Crea un libro en donde se crean las siguientes variables
        _nombre : es el nombre del libro.
        _pais: el pais de origen del libro.
        _autor: aqui se le da un autor al libro, y en caso de no exirtir 
        un autor, se crea uno nuevo.
        ademas se pone en minuscula todos ellos
        por otro lado se mantiene la id
        
        """
        Libro._seq_Libro += 1
        self._id = Libro._seq_Libro
        self._nombre = nombre.title()
        self._pais = pais.title()
        self._autor = autor

    def __str__(self):
        return f'Libro(Nombre: {self._nombre}\n\tPais: {self._pais}\n\tAutor: {self._autor.get_nombre()}\n\tId: {self._id})'

    # ArchivoId = open( self.Ruta, "ab+")
    # ArchivoId.seek(0)
    # try:
    #      self._seq_Libro = pickle.load(ArchivoId)
    #
    # finally:
    #     del self._seq_Libro
    #
    # Libro._seq_Libro += 1
    # self._id = self._seq_Libro
    # Archivo = open(self.Ruta, "ab")
    # pickle.dump(self._seq_Libro, Archivo)
    # Archivo.close
    # del Archivo
