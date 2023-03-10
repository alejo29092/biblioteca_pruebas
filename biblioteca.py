# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:40:14 2023

@author: alejo
"""
import pickle


class Biblioteca:
    """
    Esta 
    """
    _libros = []
    _libros_prestados = []
    _autores = []
    _estudiantes = []

    _ruta_autores = "persistencia_autores"
    _ruta_libros = "persistencia_libros"

    def __init__(self, nombre: str):
        self._nombre = nombre
        self._cargar_autores()
        self._cargar_libros()
        self._cargar_estudiantes()
        self._cargar_prestamos()

    def get_nombre(self):
        return self._nombre

    def buscar_libro_por_nombre(self, nombre: str):
        """
        Retorna un libro si lo encuentra en repositorio de la Biblioteca usando el nombre para buscarlo
        :param: nombre: str, string que contiene nombre del librop para ser bucado
        :return: Libro si el libro existe de lo contrario None
        """
        pass

    def buscar_libro_por_autor(self, nombre_de_autor):
        """

        """
        pass

    def registrar_libro(self):
        """
        esta funcion puede ser llamada para crear un nuevo libro
        y en caso de que el autor no este registrado, crearlo

        """
        nombre_autor = input('pon el nombre del autor ')

        self._verificar_existencia_autor(nombre_autor)

        Libros = Libro
        Libros.autor = input('introduce el autor: ')
        Libros.nombre=input('introduce el nombre del libro: ')
        Libros.pais=input('introduce el pais de origen del libro: ')
        self.AgregarLibro(Libros)
        self.GuardarLibros()

    def _verificar_existencia_autor(self, nombre_autor):
        """

        """

    def _cargar_autores(self):
        ArchivoId = open(self.Ruta2, "ab+")
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

    def _cargar_libros(self):

            with open(self._ruta_libros, "ab+") as archivo_libros: # TODO: Asegurarse de que "ab+" sea el correcto para leer
                archivo_libros.seek(0)

                try:
                    self._libros = pickle.load(archivo_libros)
                    print(f"{len(self._libros)} libros cargados ")
                except EOFError as e:
                    print("No se han cargado libros previos")
                    print(f"Error -> {e}")



