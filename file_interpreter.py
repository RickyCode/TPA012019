from os import listdir, mkdir, chdir

class FileInterpreter():

    def __init__(self, file_path, has_header=True):
        self.file = file_path
        self.has_heather = has_header
        self.file_lines = []
        self.rules = []

    def add_rule(self, positions_iterable, callable):
        # El iterable de posiciones debe considerar las posiciones de los datos de izquierda a derecha contando desde 1
        # Puede ser una lista, tupla, o cualquier otro iterable
        # "callable" puede ser una función, un método o una clase
        self.rules.append((positions_iterable, callable))

    def read_file(self):
        with open(self.file, 'r', encoding='utf-8') as archivo:
            lines = archivo.readlines()
            if self.has_heather:
                for i in range(1, len(lines)):
                    self.file_lines.append(lines[i].strip().split(','))
            else:
                for line in lines:
                    self.file_lines.append(line.strip().split(','))

    def aply_rules(self):
        # Se recorren todas las reglas:
        for rule in self.rules:
            # Por cada regla se recorren todas las lineas del archivo:
            for line in self.file_lines:
                # Por cada linea del archivo se entrega sus parametros a las funciones correspondientes:
                params = []
                # Se toman de la lista con los datos de la línea del archivo todos los datos en las posiciones
                # indicadas en la regla.
                for num in rule[0]:
                    params.append(line[num-1])
                # Se ejecuta el "callable" correspondiente con los parámetros correspondientes:
                rule[1](*params)

    def start(self):
        self.read_file()
        self.aply_rules()

if __name__ == '__main__':
    acciones_file = FileInterpreter('data/acciones.csv')
    acciones_file.add_rule([3], print)
    acciones_file.start()

