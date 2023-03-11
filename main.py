from biblioteca import Biblioteca


def menu():
    """
    da un menu de opciones y sus respectivors numeros para
    ser usada
    """
    seleccionar = 0
    while seleccionar != 12:

        print('Bienvenido al menú de la biblioteca')
        print('Primera versión 1.0')
        print('Elige una de las opciones')
        print('-'*40)
        print('1.) Registar un libro')
        print('2.) Registar un estudiante')
        print('3.) Buscar un libro por su nombre')
        print('4.) Bucar libro por el nombre del autor')
        print('5.) Buscar un estudiante')
        print('6.) Bucar un autor')
        print('7.) Mostrar todos los libros')
        print('8.) Pedir un libro prestado')
        print('9.) devolver un libro ')
        print('10.) Cuantos ejemplares hay de cada libro')
        print('11.) Cuantos ejemplares hay prestados ')

        print('12.) Salir')

        # TODO: falta agregar la funcion de agregar un autor
        # TODO: falta agregar la funcion de buscar libro por nombre
        # TODO: falta agregar la funcion de buscar libro por nombre de autor

        biblioteca = Biblioteca('Biblioteca Parque Educativo')

        print(biblioteca)

        seleccionar = int(input('Elige una opcion: '))
        if seleccionar == 1:
            biblioteca.registrar_libro()
        elif seleccionar == 2:
            biblioteca.registar_estudiante()
        elif seleccionar == 3:
            libro_buscar= input('pon el nombre del autor')
            biblioteca.buscar_libro_por_id(libro_buscar)
        elif seleccionar == 4:
             autores_filtrar = input('pon el nombre del autor')
             biblioteca.bucar_libro_por_autor(autores_filtrar)
        # elif seleccionar == 5:
        #     biblioteca.()
        # elif seleccionar ==
        elif seleccionar == 7:
            biblioteca.mostrar_libros()
        #
        # elif seleccionar == 7:
        #     biblioteca.()
        # elif seleccionar == 8:
        # biblioteca.()
        # elif seleccionar == 9:
        #     biblioteca.()
        # elif seleccionar == 10:
        #     biblioteca.()
        # elif seleccionar ==11:
        #     biblioteca.()

        print('-'*40)


# def RegistarEstudiante():
#     estudiantes = Estudiante()
#     estudiantes.nombre = input('introduce el nombre del estudiante')
#
#
# def BuscarEstudiante():
#     print('x')
#
#
# def BuscarAutor():
#     id_libro = int(input('ingresar id del libro a buscar'))
#     for ibros in listas:
#         if libros.autor == id_libro:
#             print(libros.nombre, ',', ',', libros.autor, ',', libros.pais)
#
#
# def MostrarLibros():
#     print(ListaDeLibros.MostrarLibroGuardado())
#


if __name__ == '__main__':
    menu()
