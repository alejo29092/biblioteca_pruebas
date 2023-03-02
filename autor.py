
class Autor:
    _seq_id = 0

    def __init__(self, nombre, nacianalidad: str):
            self._id = self._seq_id
            Autor._seq_id += 1

            self._nombre = nombre
            self._nacionalidad = nacianalidad
        
    def getNombre (self):
            return self._nombre
    
    def getNacionalidad (self):
            return self._nacionalidad
    
    def getId (self):
            return self._id
    def __str__(self):
        return (self._nombre, self._nacionalidad, self._id)