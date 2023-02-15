#!/usr/bin/python
#-*- coding: utf-8 -*-

from Laberinto import Laberinto
from Habitacion import Habitacion
from Puerta import Puerta
from Pared import Pared


class Juego:
    def _init_(self):
        self.laberinto = None
        
        
    def fabricarLaberinto(self):
        return Laberinto()
    
    def laberinto2HabitacionesFM(self):
        self.laberinto=self.fabricarLaberinto()
        #TODO
        
    def laberinto2Habitaciones(self):
        self.laberinto = Laberinto()
        
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)
        hab3 = Habitacion(3)
        
        puerta = Puerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2
        
        hab1.sur = puerta
        hab2.norte= puerta
        
        hab1.norte = Pared()
        hab2.este = Pared()
        hab1.oeste = Pared()
        
        hab2.sur = Pared()
        hab2.este = Pared()
        hab3.oeste = Pared()
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        
juego = Juego()
juego.laberinto2Habitaciones()