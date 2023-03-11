LibrosGuardados = []


class Autor:
    _seq_id = 0
    GuardadosId = []

    def __init__(self, nombre):
        """
        Esta clase nos da el nombre del autor y si el autor no esta registrado 
        su nacionalidad y crea al nuevo autor
        Guarda en un documento de texto los libros con sus autores 

        """
        self._id = Autor._seq_id
        Autor._seq_id += 1
        self._nombre = nombre

    def autor_verificar(self, nombre):
        pass

    def get_nombre(self):
        return self._nombre

    def __str__(self):
        return f"{self._nombre}, {self._id}"

#
# class ListaDeLibros:
#
#     def AgregarLibro(self, e):
#         self.LibrosGuardados.append(e)
#         self.GuardarLibros()
#
#     def MostrarLibroGuardado(self):
#         for e in self.LibrosGuardados:
#             print(e)
#
#     def GuardarLibros(self):
#         """
#         esta funcion actualiza el doncumento donde se encuentran
#         los libros guardados
#         """
#         Archivo = open(self.Ruta, "ab")
#         pickle.dump(self.LibrosGuardados, Archivo)
#         Archivo.close
#         del Archivo
#
#     def BuscarLibroId(self):
#         id_libro = int(input('ingresar id del libro a buscar'))
#         for libros in LibrosGuardados:
#             if libros._id == id_libro:
#                 print(self.libros.nombre, ',', ',', self.libros.autor, ',', self.libros.pais, ',', self.libros.id)
#
#     def BuscarLibro(self):
#         id_libro = int(input('ingresar id del libro a buscar'))
#         for self.Libros in LibrosGuardados:
#             if id_libro == self._seq_Libro:
#                 print(self.Libros.nombre, ',', ',', self.Libros.autor, ',', self.Libros.pais)
