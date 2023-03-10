from libro import Libro
LibrosGuardados = []
import pickle


class Autor():
    _seq_id = 0
    GuardadosId = []
    Ruta2 = "biblioteca_Id_Autor"
    Ruta = "biblioteca_libros"
    nacionalidad=str


    def __init__(self, nombre):
        """
        Esta clase nos da el nombre del autor y si el autor no esta registrado 
        su nacionalidad y crea al nuevo autor
        Guarda en un documento de texto los libros con sus autores 

        """
        ArchivoLibros = open( self.Ruta, "ab+")
        ArchivoLibros.seek(0)
            
        # TODO:leer un poco sobre los context manager. with 
        
          # with open(Ruta, "ab+") as archivoLibros:
            
        try:
            self.LibrosGuardados = pickle.load(ArchivoLibros)
            print(f"{len(self.LibrosGuardados)} libros guardados ")
        except EOFError as e:
            print("no se han cargado libros previos")
            print(f"Error -> {e}")
        finally:
            del ArchivoLibros
     
        
        self._id = self._seq_id
        self._seq_id += 1
        self._nombre = nombre
        
    def AutorVerificar(self):
        for nombre in LibrosGuardados:
            if nombre != LibrosGuardados.autor:
                print("El autor del libro no estaba registrado, por lo cual lo debes registrar")
                self.Autor.nombre = input('pon el nombre común del autor: ')
                self.nacionalidad = input('pon la nacionalidad del autor: ')
                self._nacionalidad = nacionalidad
            else:
                pass
        
        
        ArchivoId = open( self.Ruta2, "ab+")
        ArchivoId.seek(0)
        try:
            self.GuardadosId = pickle.load(ArchivoId)
              
        finally:
            del ArchivoId
        self._id = self._seq_Libro 
        Libro._seq_Libro += 1
        Archivo = open(self.Ruta2, "ab")
        pickle.dump(self.LibrosId, Archivo)
        Archivo.close
        del Archivo  

            
    def __str__(self):
        return f"{self._nombre} , {self._nacionalidad}, {self._id}"
    
class ListaDeLibros:
   
    def AgregarLibro(self,e):
        self.LibrosGuardados.append(e)
        self.GuardarLibros()
    
    
    def MostrarLibroGuardado(self):
        for e in self.LibrosGuardados:
            print(e)
            
            
    def GuardarLibros(self):
        """
        esta funcion actualiza el doncumento donde se encuentran
        los libros guardados 
        """
        Archivo = open(self.Ruta, "ab")
        pickle.dump(self.LibrosGuardados, Archivo)
        Archivo.close
        del Archivo
         
        
    def RegistrarLibro(self):
        """
        esta funcion puede ser llamada para crear un nuevo libro
        y en caso de que el autor no este registrado, crearlo

        """
        VariableAutor = input('pon el nombre del autor ')
        
        self.AutorVerificar(VariableAutor)
        Libros = Libro
        Libros.autor = input('introduce el autor: ')
        Libros.nombre=input('introduce el nombre del libro: ')
        Libros.pais=input('introduce el pais de origen del libro: ')
        self.AgregarLibro(Libros)
        self.GuardarLibros()
        
        
    def BuscarLibroId (self):
        id_libro = int(input('ingresar id del libro a buscar'))
        for libros in LibrosGuardados :
            if libros._id == id_libro:
                print(self.libros.nombre,',', ',',self.libros.autor,',', self.libros.pais, ',', self.libros.id)
                
                
    def BuscarLibro(self):
        id_libro = int(input('ingresar id del libro a buscar'))
        for self.Libros in LibrosGuardados :
            if id_libro == self._seq_Libro:
                print(self.Libros.nombre,',', ',',self.Libros.autor,',', self.Libros.pais)
               