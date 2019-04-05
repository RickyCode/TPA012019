class Edificio():
    # Necesario para su construcción:
    madera = 0
    piedra = 0
    oro = 0
    trabajadores = 0
    cant_turnos = 0
    p_oro = 0
    p_madera = 0
    p_piedra = 0
    hp_inicial = 0

    def __init__(self):
        self.hp = self.hp_inicial
        self.construccion_hasta = 0

class CentroUrbano(Edificio):
    # Primer edificio
    # 1 por civilización
    # Si es destruido termina el juego
    

    def __init__(self):
        Edificio.__init__(self)

class Cuartel(Edificio):
    # Las civilizaciones no parten con cuaretel
    # Se puede tener uno a la vez

    def __init__(self):
        Edificio.__init__(self)

class DCCowork(Edificio):
    # No se parte con uno
    # Solo se puede tener uno a la vez

    def __init__(self):
        Edificio.__init__(self)

class Muralla(Edificio):
    # No genera personas
    # Se pueden construir tantos como se quiera
    # Provee defenza

    def __init__(self):
        Edificio.__init__(self)


if __name__ == '__main__':
    Edificio.madera = 10
    print(Edificio.madera)
    
    CentroUrbano.madera = 20
    print(CentroUrbano.madera)

    Muralla.madera = 40
    print(Muralla.madera)
    
    print(Edificio.madera)
    print(CentroUrbano.madera)
    print(Muralla.madera)