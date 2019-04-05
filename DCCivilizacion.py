
from Civilizacion import Civilizacion
from menu import Menu
from file_interpreter import FileInterpreter
from Edificio import CentroUrbano, Cuartel, DCCowork, Muralla

class DDCivilizacion():
    # Esta clase se encarga de gestionar los archivos y carpetas, interpretar la
    # infomración necesaria para partir el juego, y, si corresponde, guardar.
    # Esta clase además muestra el menú incial e inicia la partida.

    def __init__(self):
        self.partida_actual = None
        self.menu_inicial()

    def crear_civilizacion(self, id, cto_urbano, cuartel, dccowork, muralla, trabajadores, soldados, ayudantes,
                           oro, madera, piedra, pts_tecnologia, usuario):
        bolean = {'True': True,
                 'False': False}
        Civilizacion(int(id),
                     bolean[cto_urbano],
                     bolean[cuartel],
                     bolean[dccowork],
                     int(muralla),
                     int(trabajadores),
                     int(soldados),
                     int(ayudantes),
                     int(oro),
                     int(madera),
                     int(piedra),
                     int(pts_tecnologia),
                     bolean[usuario],
                     )

    def config_edificios(self, nombre, turnos, c_trab, c_oro, c_madera,
                         c_piedra, hp, p_oro, p_madera, p_piedra):
        edificios = {'centro_urbano': CentroUrbano,
                     'cuartel': Cuartel,
                     'DCCowork': DCCowork,
                     'muralla': Muralla}
        edificios[nombre].madera = int(c_madera)
        edificios[nombre].piedra = int(c_piedra)
        edificios[nombre].oro = int(c_oro)
        edificios[nombre].trabajadores = int(c_trab)
        edificios[nombre].cant_turnos = int(turnos)
        edificios[nombre].p_oro = int(p_oro)
        edificios[nombre].p_madera = int(p_madera)
        edificios[nombre].p_piedra = int(p_piedra)
        edificios[nombre].hp = int(hp)



    def leer_archivos_partida_nueva(self):
        # Edificios:
        archivo_edificios = FileInterpreter('data/edificios.csv')
        archivo_edificios.add_rule(range(1,11), self.config_edificios)
        archivo_edificios.start()
        # Civilizaciones:
        archivo_civilizaciones = FileInterpreter('data/civilizaciones.csv')
        archivo_civilizaciones.add_rule([1]+list(range(3, 15)), self.crear_civilizacion)
        archivo_civilizaciones.start()


    def crear_partida(self):
        nom_jugador = str(input('Ingresa tu nombre: '))
        self.partida_actual = Partida(nom_jugador)
        self.leer_archivos_partida_nueva()
        self.partida_actual.comenzar()


    def guardar_partida(self):
        pass

    def hay_partidas_guardadas(self):
        # Retorna true si hay
        # False de lo contrario
        return False

    def cargar_partida(self):
        # Algo
        self.partida_actual.comenzar()

    def cerrar_juego(self):
        print('entrp a cerrar juego')
        pass


    def menu_inicial(self):
        if self.hay_partidas_guardadas():
            menu_inicial = Menu()
            menu_inicial.add('Nueva Partida', self.crear_partida)
            menu_inicial.add('Cargar Partida', self.cargar_partida)
        else:
            menu_inicial = Menu(user_info='No hay partidas guardadas.\nElige una opción:')
            menu_inicial.add('Nueva Partida', self.crear_partida)
        menu_inicial.add('Cerrar Juego', self.cerrar_juego)
        menu_inicial.show()




class Partida():
    # esta clase gestiona cada partida, tanto la civilización del usuario como las
    # civilizaciones controladas automáticamente.

    def __init__(self, nombre_jugador):
        self.nombre_jugador = nombre_jugador
        self.jugar = True
        self.civilizacion_jugador = None # Las demás civilizaciones se guargan en la clase Civilizacion
        self.__contador_turnos = 1
        self.en_turno = True

    # def crear_civilizacion(self, tipo):
    #     self.civilizacion_jugador = Civilizacion(tipo)
    #     self.comenzar()

    # def crear_civilizacion(self, id, tipo, cto_urbano, cuartel, dccowork, muralla, trabajadores, soldados, ayudantes,
    #                        oro, madera, piedra, pts_tecnologia, usuario):

    def seleccionar_civilizacion(self, tipo):
        for civi in Civilizacion.lista_civilizaciones:
            if civi.tipo == tipo:
                civi.usuario = True
                self.civilizacion_jugador = civi
                print(civi)

    def cambio_turno(self):
        self.__contador_turnos +=1
        Civilizacion.turno_actual = self.__contador_turnos


    def elegir_civilización(self):
        menu_civilizaciones = Menu(user_info='Selecciona tu cvilización:')
        menu_civilizaciones.add('DCC', self.seleccionar_civilizacion, 0)
        menu_civilizaciones.add('La Comarca', self.seleccionar_civilizacion, 1)
        menu_civilizaciones.add('Cobreloa', self.seleccionar_civilizacion, 2)
        menu_civilizaciones.show()

    def comenzar(self):
        while self.jugar:
            if self.civilizacion_jugador:
                    self.menu_turno()
                    # Acciones de las otras civilizaciones que no son del usuario:
                    print('El turno {} ha finalizado'.format(self.__contador_turnos))
                    self.cambio_turno()
            else:
                self.elegir_civilización()

    def menu_cont_edificio(self):
        menu_edificio = Menu(user_info='Selecciona uno de los edificios que puedes construir:')
        if not self.civilizacion_jugador.cuartel:
            menu_edificio.add('Cuartel', self.civilizacion_jugador.construir_edificio, 1)
        if not self.civilizacion_jugador.DCCowork:
            menu_edificio.add('DCCowork', self.civilizacion_jugador.construir_edificio, 2)
        menu_edificio.add('Muralla', self.civilizacion_jugador.construir_edificio, 3)
        menu_edificio.show()




    def guardar(self):
        pass

    def finalizar_turno_usuario(self):
        self.en_turno = False

    def finalizar_partida(self):
        menu_salir = Menu()
        menu_salir.add('Guardar y Salir', self.guardar)
        menu_salir.add('Salir sin Guardar', print, 'no se guardó la partida')
        menu_salir.show()
        self.finalizar_turno()
        self.jugar = False

    def menu_turno(self):
        self.en_turno = True
        menu_turno = Menu('Turno {}\nSelecciona una opción: '.format(self.__contador_turnos))
        menu_turno.add('Recolectar Recursos', print, 'se selecciono recolectar recursos')
        menu_turno.add('Crear Personas', print, 'se selecciono Crear Personas')
        menu_turno.add('Crear Edificios', self.menu_cont_edificio)
        menu_turno.add('Atacar', print, 'se selecciono Atacar')
        menu_turno.add('Esperar Siguiente Turno', self.finalizar_turno_usuario)
        menu_turno.add('Estadísticas', print, 'se selecciono Estadísticas')
        menu_turno.add('Guardar', print, 'se selecciono Guardar')
        menu_turno.add('Salir', self.finalizar_partida)
        while self.en_turno:
            menu_turno.show()

if __name__ == '__main__':
    DDCivilizacion()

