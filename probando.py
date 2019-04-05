
class Edificio():

    def __init__(self):
        pass

    @classmethod
    def metodo_clase(cls):
        print('Metodo de la clase')

    def metodo_instancia(self):
        print('Método de la instancia')


if __name__ == '__main__':

    edificio1= Edificio()
    edificio1.metodo_instancia()


    Edificio.metodo_clase()