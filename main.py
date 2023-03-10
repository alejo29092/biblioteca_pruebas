from autor import ListaDeLibros
from biblioteca import Biblioteca


def menu():
    """
    da un menu de opciones y sus respectivors numeros para
    ser usada
    """
    seleccionar = 0
    while seleccionar != 7:

        print('Bienvenido al menú de la biblioteca')
        print('Primera versión 1.0')
        print('Elige una de las opciones')
        print('-----------------------------------------')
        print('1.) Registar un libro')
        print('2.) Registar un estudiante')
        print('3.) Buscar un libro por su id')
        print('4.) Buscar un estudiante')
        print('5.) Bucar un autor')
        print('6.) Mostrar libros')
        print('7.) Salir')

        # TODO: falta agregar la funcion de agregar un autor
        # TODO: falta agregar la funcion de buscar libro por nombre
        # TODO: falta agregar la funcion de buscar libro por nombre de autor

        biblioteca = Biblioteca('Biblioteca Parque Educativo')

        seleccionar = int(input('Elige una opcion: '))
        if seleccionar == 1:
            biblioteca.registrar_libro()
        elif seleccionar == 2:
            biblioteca.registar_estudiante()
        elif seleccionar == 3:
            biblioteca.buscar_libro_por_id()
        elif seleccionar == 4:
            BuscarEstudiante()
        elif seleccionar == 5:
            BuscarAutor()
        elif seleccionar == 6:
            MostrarLibros()
        print('---------------------------------------')


libros = Libro


def RegistarEstudiante():
    estudiantes = Estudiante()
    estudiantes.nombre = input('introduce el nombre del estudiante')


def BuscarEstudiante():
    print('x')


def BuscarAutor():
    id_libro = int(input('ingresar id del libro a buscar'))
    for ibros in listas:
        if libros.autor == id_libro:
            print(libros.nombre, ',', ',', libros.autor, ',', libros.pais)


def MostrarLibros():
    print(ListaDeLibros.MostrarLibroGuardado())




if __name__ == '__main__':
    menu()