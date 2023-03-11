# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:41:07 2023

@author: alejo
"""


class Estudiante:
    _seq_Libro = 0

    def __init__(self, nombre: str):
        self._id = self._seq_Libro
        self._seq_Libro += 1
        self._nombre = nombre

    def getNombreEstudiante(self):
        return self._nombre

    def RegistarEstudiante():
        estudiantes = Estudiante()
        estudiantes.nombre = input('introduce el nombre del estudiante')
