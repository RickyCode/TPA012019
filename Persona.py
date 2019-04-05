from abc import ABC, abstractmethod, abstractproperty
from random import randint
from data.constantes import *

class Persona(ABC):

    @property
    @abstractmethod
    def _hp(self):
        pass

class Trabajador():
    # Recolecta recursos y construye edificios
    # Una tarea a la vez

    def __init__(self):
        self._hp = randint(MIN_HP_PERSONA, MAX_HP_PERSONA)
        self.ocupado_hasta = 0 # Ultimo turno en el que estará ocupado

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, daño):
        self._hp -= daño

    def recolectar_recurso(self):
        # Recolecta random(Min_CANTIDAD_RECURSO, MAX_CANT_RECURSO)
        # La cantidad de recursos extraido estará disponible en el sgte turno
        return randint(MIN_HP_PERSONA, MAX_HP_PERSONA)

class Soldado(Persona):
    # Entrenados en el cuartel
    # Capacidad de atacar a otras civilizaciones
    # Poder de fuerza random(MIN_ATAQUE_SOLDADO, MAX_ATAQUE_SOLDADO)

    def __init__(self):
        self._hp = randint(MIN_HP_PERSONA, MAX_HP_PERSONA)
        self.fuerza = randint(MIN_ATAQUE_SOLDADO, MAX_ATAQUE_SOLDADO)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, daño):
        self._hp -= daño

class Ayudante(Persona):
    # Generado en el DCCoworck
    # IQ = random(MIN_IQ_AYUDANTE, MAX_IQ_AYUDANTE)

    def __init__(self):
        self._hp = randint(MIN_HP_PERSONA, MAX_HP_PERSONA)
        self.iq = randint(MIN_IQ_AYUDANTE, MAX_IQ_AYUDANTE)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, daño):
        self._hp -= daño

