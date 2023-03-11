# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:42:47 2023

@author: alejo
"""

"""LibrosPosesion = list()
LibrosPrestamo = list()
LibrosPosesion.append(libros)

 for libros in LibrosPosesion:
    print('el libro',libros.nombre,' de Autor ', libros.autor, ' y fue echo en ', libros.pais)
    """
# import pickle
#
#
# class ListaDeLibros:
#     LibrosGuardados = []
#     Ruta = "biblioteca_libros"
#
#     def __init__(self):
#         ArchivoLibros = open(self.Ruta, "ab+")
#         ArchivoLibros.seek(0)
#
#         # TODO:leer un poco sobre los context manager. with
#
#         # with open(Ruta, "ab+") as archivoLibros:
#
#         try:
#             self.LibrosGuardados = pickle.load(ArchivoLibros)
#             print(f"{len(self.LibrosGuardados)} libros guardados ")
#         except EOFError as e:
#             print("no se han cargado libros previos")
#             print(f"Error -> {e}")
#         finally:
#             del ArchivoLibros
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
#         Archivo = open(self.Ruta, "ab")
#         pickle.dump(self.LibrosGuardados, Archivo)
#         Archivo.close
#         del Archivo
#
#
# """"for libros in self.librosGuardados :
#             if libros.autor == :
#                 print(libros.nombre,',', ',',libros.autor,',', libros.pais)
#         if autor == autor:
#             continue
#         if autor != libros:
#             autores.nombre = input('ingrese nuevamente el nombre del nuevo autor')
#             autores.nacionalidad = input('ingrese la nacionalidad del autor')
#
# def getNombre (self):
#     return self._nombre
#
# def getInfoLibro(self):
#     return self._nombre
#     return self._pais
#     return self._autor
#
#
#
# """
#
# """
# libro1 = Libro('GAbriel Garcia', 'cien años de soledad', 'Colombia', False)
# libro2 = Libro('Gabriel Garcia', 'cien años de soledad', 'Colombia', False)
# LibrosAgregar = ListaDeLibros()
# LibrosAgregar.AgregarLibro(libro1)
# LibrosAgregar.AgregarLibro(libro2)
# LibrosAgregar.GuardarLibros()
#
# LibrosAgregar.MostrarLibroGuardado()
#
# LibrosAgregar.RegistarLibro()
# """
