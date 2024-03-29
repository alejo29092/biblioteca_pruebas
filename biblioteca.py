 # -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:40:14 2023

@author: alejo
"""
import pickle
from collections import deque
from Estudiante import Estudiante
from autor import Autor
from libro import Libro


class Biblioteca:
    """
    Esta es la clase que lleva la mayoria de funciones de la aplicación
    """

    _ruta_autores = "persistencia_autores.repo"
    _ruta_libros = "persistencia_libros.repo"
    _ruta_estudiantes = "persistencia_estudiantes.repo"
    _ruta_prestados = "persistencia_prestamos.repo"

    def __init__(self, nombre: str):
        self._libros = []
        self._libros_prestados = []
        self._autores = []
        self._estudiantes = []

        self._nombre = nombre
        self._cargar_autores()
        self._cargar_libros()
        self._cargar_estudiantes()
        self._cargar_prestados()

    def get_nombre(self):
        return self._nombre

    def verificar_existencia_autor(self, nombre_autor) -> bool:
        """
        Está función revisa si el nombre del autor se encuentra en la lista _autores
        y en caso de que no lo esté pide registrarlo

        """
        for autor in self._autores:
            if nombre_autor.title() == autor.get_nombre().title():
                return True
        return False

    def _get_autor(self, nombre_autor) -> Autor:
        """
        Dado un nombre busca un autor en self._autores y lo retorna como un Autor
        """
        # autor_encontrado = None
        # for autor in self._autores:
        #     if autor.get_nombre() == nombre_autor:
        #         autor_encontrado = autor
        #         break

        autores = list(filter(lambda autor: autor.get_nombre() == nombre_autor, self._autores))

        if autores:
            return autores[0]
        else:
            None

    def _crear_autor(self, nombre):
        """
        Esta función crea un autor y llamaba la función para guardarlo
        """
        autor = Autor(nombre=nombre)
        self._guardar_autor(autor)
        return autor

    def _cargar_autores(self):
        """
        Carga los autores guardados en la lista
        _autores
        """
        try:
            print("Cargando Autores desde disco")
            with open(Biblioteca._ruta_autores, "rb") as archivo_autores:
                self._autores = pickle.load(archivo_autores)
            print(f"{len(self._autores)} Autores cargados ")
        except EOFError as e:
            print("No se han cargado autores previos")
            print(f"Error -> {e}")
        except (IOError, OSError):
            print("Creando un archivo para repo de autores ya que no existia")
            with open(Biblioteca._ruta_autores, "wb") as archivo_autores:
                self._autores = []
                pickle.dump(self._autores, archivo_autores)

    def _guardar_autor(self, autor: Autor):
        """
        Esta función guarda al autor en el repositorio
        """
        self._autores.append(autor)
        self._guardar_autores_repo()

    def _guardar_autores_repo(self):
        """"
        Agrega el nuevo autor a la lista _autores y lo carga en el documento
        de los autores
        """
        with open(self._ruta_autores, "wb") as archivo:
            pickle.dump(self._autores, archivo)

    def registrar_libro(self):
        """
        esta funcion puede ser llamada para crear un nuevo libro
        y en caso de que el autor no este registrado, crearlo
        """
        nombre_autor = input('Pon el nombre del autor ')

        autor_existe = self.verificar_existencia_autor(nombre_autor)

        if autor_existe:
            autor = self._get_autor(nombre_autor)
        else:
            autor = self._crear_autor(nombre_autor)

        nombre_libro = input("Ingresa el nombre del Libro: ")
        pais_libro = input("Ingresa el Pais del Libro: ")
        libros_cantidad= input("ponga rl numro de libros existentes")

        nuevo_libro = Libro(nombre=nombre_libro, autor=autor, pais=pais_libro, cantidad=libros_cantidad)

        self._guardar_libro(nuevo_libro)

    def _cargar_libros(self):
        """"
        Carga los libros guardados en la lista
        _libros

        """
        try:
            print("Cargando Libros desde disco")
            with open(Biblioteca._ruta_libros, "rb") as archivo_libros:
                self._libros = pickle.load(archivo_libros)
            print(f"{len(self._libros)} libros cargados ")
        except EOFError as e:
            print("No se han cargado libros previos")
            print(f"Error -> {e}")
        except (IOError, OSError):
            print("Creando un archivo para repo de libros ya que no existia")
            with open(Biblioteca._ruta_libros, "wb") as archivo_libros:
                self._libros = []
                pickle.dump(self._libros, archivo_libros)

    def _guardar_libro(self, libro: Libro):
        """
        Esta función guarda los libros creados en la lista libros y además los guarda directamente
        en el repositorio
        """
        self._libros.append(libro)
        self._guardar_libros_repo()

    def _guardar_libros_repo(self):
        """
        Esta función guarda los libros en el repositorio
        :return:
        """
        with open(self._ruta_libros, "wb") as archivo:
            pickle.dump(self._libros, archivo)

    def mostrar_libros(self):
        """
        Esta función muestra todos los libro almacenados en la lista: _libros

        """
        print('-' * 100)
        print('Libros de la Biblioteca : ')

        if self._libros:
            deque(map(print, self._libros))
            # print(self._libros)
        else:
            print("No hay libros en la Biblioteca")

        print('-' * 100)
        print('-' * 100)

    def buscar_libro_por_autor(self, nombre_autor) -> Estudiante:
        """
        Esta función busca todos los libros que hallan por nombre del mismo autor
        """
        nombre_autor.title()
        for i in self._libros:
            if i._autor == nombre_autor:
                print(f"{i.__str__}")

    def buscar_libro_por_nombre(self, nombre_libro):
        """
        Retorna un libro si lo encuentra en repositorio de la Biblioteca usando el nombre para buscarlo
        :param: nombre: str, string que contiene nombre del librop para ser bucado
        :return: Libro si el libro existe de lo contrario None
        """
        nombre_libro.title()
        for i in self._libros:
            if i._nombre == nombre_libro:
                print(f"{i.__str__}")

    def _cargar_estudiantes(self):
        """"
          Carga los autores guardados en la lista
        _estudiantes

        """
        try:
            print("Cargando Libros desde disco")
            with open(Biblioteca._ruta_estudiantes, "rb") as archivo_estudiantes:
                self._estudiantes = pickle.load(archivo_estudiantes)
            print(f"{len(self._estudiantes)} libros cargados ")
        except EOFError as e:
            print("No se han cargado libros previos")
            print(f"Error -> {e}")
        except (IOError, OSError):
            print("Creando un archivo para repo de libros ya que no existia")
            with open(Biblioteca._ruta_estudiantes, "wb") as archivo_estudiantes:
                self._estudiantes = []
                pickle.dump(self._estudiantes, archivo_estudiantes)

    def registar_estudiante(self, nombre_estudiante):
        nombre_estudiante.title()
        self._guardar_estudiante(nombre_estudiante)

    def _guardar_estudiante(self, estudiante):
        """
        Esta función guarda a los estudiantes en el repositorio
        """
        self._estudiantes.append(estudiante)
        self._guardar_estudiante_repo()

    def _guardar_estudiante_repo(self):
        """
        Está función guarda a los estudiantes en el repositorio
        """
        with open(self._ruta_estudiantes, "wb") as archivo:
            pickle.dump(self._estudiantes, archivo)

    def buscar_estudiante(self, id_del_estudiante):
        """
        Está función busca la Id de un estudiante en la lista _estudiantes
        """
        for i in self._estudiantes:
            if i._id == id_del_estudiante:
                print(f"{i.__str__}")
        pass

    #  def cofirmar_estudiante(self,nombre_estudiante) -> Estudiante:
    #
    #
    #       if estudiantes:
    #          return estudiantes[0]
    #
    #        else:
    #            None

    def _cargar_prestados(self):
        """"
        Carga los libros que están prestados en la siguiente lista
        _libros_prestados
        """
        try:
            print("Cargando Libros desde disco")
            with open(Biblioteca._ruta_prestados, "rb") as archivo_prestados:
                self._libros_prestados = pickle.load(archivo_prestados)
            print(f"{len(self._libros_prestados)} libros cargados ")
        except EOFError as e:
            print("No se han cargado libros previos")
            print(f"Error -> {e}")
        except (IOError, OSError):
            print("Creando un archivo para repo de libros ya que no existia")
            with open(Biblioteca._ruta_prestados, "wb") as archivo_prestados:
                self._libros_prestados = []
                pickle.dump(self._libros_prestados, archivo_prestados)

    def __str__(self):
        return f"Biblioteca(nombre: {self._nombre}, nro_libros: {len(self._libros)})"
