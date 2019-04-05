from Edificio import CentroUrbano, Cuartel, DCCowork, Muralla
from Persona import Trabajador, Soldado, Ayudante
from Recurso import Recurso


class Civilizacion():
    lista_civilizaciones = []
    turno_actual = 0

    def creacion_inicial_personas(self, c_trabajadores, c_soldados, c_ayudantes):
        # Creación de personas en base a los parámetros recibidos:
        if c_trabajadores > 0:
            self.crear_personas(0, c_trabajadores, True)
        if c_soldados > 0:
            self.crear_personas(1, c_soldados, True)
        if c_ayudantes > 0:
            self.crear_personas(2, c_ayudantes, True)

    def creacion_inicial_edificios(self, b_cto_urbano, b_cuartel, b_dccowork, c_murallas):
        if b_cto_urbano:
            self.centro_urbano = CentroUrbano()
        if b_dccowork:
            self.DCCowork = DCCowork()
        if c_murallas > 0:
            for i in c_murallas:
                self.murallas.append(Muralla())

    def __init__(self, tipo, b_cto_urbano, b_cuartel, b_dccowork, c_murallas, c_trabajadores, c_soldados, c_ayudantes,
                 oro, madera, piedra, pts_tecnolo, usuario=False):
        self.tipo = tipo # {0: 'DCC', 1: 'La Comarca', 2: 'Cobreloa'}
        self.soldados = []
        self.trabajadores = []
        self.ayudantes = []
        # Recursos:
        self.c_piedra = piedra
        self.c_madera = madera
        self.c_oro = oro
        # Edificios
        self.centro_urbano = None
        self.cuartel = None
        self.DCCowork = None
        self.murallas = []
        # Investigación:
        self.puntos_tecnologia = pts_tecnolo
        # Pertenece a un usuario:
        self.usuario = usuario
        # Funciones iniciales
        self.creacion_inicial_personas(c_trabajadores, c_soldados, c_ayudantes)
        self.creacion_inicial_edificios(b_cto_urbano, b_cuartel, b_dccowork, c_murallas)
        # Se guarda en la lista de civilizaciones:
        Civilizacion.lista_civilizaciones.append(self)

    def __str__(self):
        civilizaciones = {0: 'DCC',
                          1: 'La Comarca',
                          2: 'Cobreloa'}
        return 'La civilizacion del usuario es: ' + civilizaciones[self.tipo]

    @property
    def poder_ataque(self):
        fuerza_soldados = sum(map(lambda soldado: soldado.fuerza, self.soldados))
        if self.tipo == 1:  # DCC
            return round(fuerza_soldados + self.puntos_tecnologia)
        elif self.tipo == 2:  # La Comarca
            return round(fuerza_soldados + (self.c_piedra / 2))
        elif self.tipo == 3:  # Cobreloa
            return round(fuerza_soldados * 1.15)

    @property
    def poder_defensa(self):
        defensa_base = sum(map(lambda soldado: soldado.hp, self.soldados)) \
                        + sum(map(lambda trabajador: trabajador.hp, self.trabajadores)) \
                        + sum(map(lambda muralla: muralla.hp, self.murallas)) \
                        + self.centro_urbano.hp + self.cuartel.hp
        if self.tipo == 1:  # DCC
            return round(defensa_base + (100 * len(self.ayudantes)))
        elif self.tipo == 2:  # La Comarca
            return round(defensa_base + (self.c_madera / 2))
        elif self.tipo == 3:  # Cobreloa
            return round(defensa_base * 1.1)
        
    @property
    def trabajadores_disponibles(self):
        contador = 0
        for trabajador in self.trabajadores:
            if trabajador.ocupado_hasta < self.turno_actual:
                contador += 1
        return contador

    def atacar(self, civilizacion_atacada):
        if self.poder_ataque > civilizacion_atacada.poder_defensa:
            civilizacion_atacada.centro_urbano.hp = 0 #Destrye el centro urbano
            # PENDIENTE: Falta implementar que una cantidad aleatoria de recursos y ayudantes
            # pase a la civilización ganadora.
        else:
            # PENDIENTE: Falta implementar que se restan los puntos de ataque a los HP de los elementos en el
            # siguiente orden:
            # Murallas > solsados > cuartel > trabajaores > centro urbano
            pass


    def defender(self):
        pass

    def investigar(self):
        pass

    def recolectar_recursos(self):
        pass

    def crear_personas(self, tipo, cantidad, inicial=False):
        personas = {0: [self.trabajadores, Trabajador],
                    1: [self.soldados, Soldado],
                    2: [self.ayudantes, Ayudante]}
        if inicial:
            for i in range(cantidad):
                personas[tipo][0].append(personas[tipo][1]())
            else:
                pass
            
    def ocupar_trabajadores(self, cant, num_turnos):
        trabajadores_reclutados = 0
        for trabajador in self.trabajadores:
            if trabajador.ocupado_hasta < self.turno_actual and trabajadores_reclutados < cant:
                trabajador.ocupado_hasta = self.turno_actual + num_turnos
                
    def se_puede_construir(self, trab_necesarios, oro_nec, piedra_nec, madera_nec):
        mensaje_base = 'NO posees suficiente{} para construir el edificio, tienes: ({}/{})'
        mensajes_error = []
        if self.trabajadores_disponibles < trab_necesarios:
            mensajes_error.append(mensaje_base.format('s trabajadores desocupados', self.trabajadores_disponibles, trab_necesarios))
        if self.c_oro < oro_nec:
            mensajes_error.append(mensaje_base.format(' oro', self.c_oro, oro_nec))
        if self.c_piedra < piedra_nec:
            mensajes_error.append(mensaje_base.format(' piedra', self.c_piedra, piedra_nec))
        if self.c_madera < madera_nec:
            mensajes_error.append(mensaje_base.format(' madera', self.c_madera, madera_nec))
        if len(mensajes_error) > 0:
            for mensaje in mensajes_error:
                print(mensaje)
            return False
        return True
        


    def construir_edificio(self, num_tipo):
        edificios  = {0: [self.centro_urbano, CentroUrbano, 'el CentroUrbano'],
                      1: [self.cuartel, Cuartel, 'el Cuartel'],
                      2: [self.DCCowork, DCCowork, 'el DCCowork'],
                      3: [self.murallas, Muralla, 'una Muralla']}
        trab_necesarios = edificios[num_tipo][1].trabajadores
        turnos_necesarios = edificios[num_tipo][1].cant_turnos
        oro_nec = edificios[num_tipo][1].oro
        piedra_nec = edificios[num_tipo][1].piedra
        madera_nec = edificios[num_tipo][1].madera
        if self.se_puede_construir(trab_necesarios, oro_nec, piedra_nec, madera_nec):
            self.ocupar_trabajadores(trab_necesarios, turnos_necesarios)
            edificios[num_tipo][0] = edificios[num_tipo][1]()
            edificios[num_tipo][0].construccion_hasta = self.turno_actual + turnos_necesarios
            self.c_oro -= oro_nec
            self.c_piedra -= piedra_nec
            self.c_madera -= madera_nec
            print('Se ha construido {}'.format(edificios[num_tipo][2]))


if __name__ == '__main__':
    for i in range(20):
        print(i)