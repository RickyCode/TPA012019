class Option:
    # Esta clase gestiona cada opción que será mostrada en el menú.
    # Es la encargada de asociar cada opción con una función/método

    def __init__(self, name, function, *func_params):
        # Recibe el nombre, el nombre de la función y los parámetros de la función.
        # Los parametros de la función se reciben con un "*" para recibir datos
        # 'desempaquetados' y 'empaquetarlos' como una lista.
        self.name = name
        self.function = function
        self.func_params = func_params  # lista

    def execute(self):
        # Esta función ejecuta la función asociada a la opción.
        # Los parametros se entregan con un "*" para 'desempaquetar' la lista.
        # OJO: Se cae si alguien pos casualidad entrega un 'funcion()' que no retorne nada en vez de 'funcion'
        self.function(*self.func_params)

    def __str__(self):
        # Esta función retorna lo que se mostrará cuandos e llame al método str()
        # sobre la instancia de la clase.
        return self.name


class Menu:
    # Clase que almacena las opciones que se mostrarán y gestiona
    # de manera 'robusta' los "inputs" del usuario.

    def __init__(self
                 , user_info='Selecciona una opción: '  # Opcional
                 , wrong_option_text=None  # Opcional
                 , input_message='Ingresa el número correspondiente: '  # Opcional
                 , multi_selection=False):  # Opcional
        self.user_info = user_info  # Instrucciones que se le muestran al usuario
        self.wrong_option_text = wrong_option_text  # Se muestra cuando el input no es válido
        self.input_message = input_message  # Se muestra cuando se le solicita al usuario su input
        self.multi_selection = multi_selection  # BOOLEAN Para que el usuario pueda seleccionar varias opciones
        self.alternatives = []  # Lista de objetos "Option"
        self.finish = False  # Usado para terminar el ciclo del menú

    def add(self, name, function, *func_params):
        # Crea nuevos opjetos "Option" y los almacena en la lista:
        self.alternatives.append(Option(name, function, *func_params))

    def set_wrong_input_mesage(self, user_input):
        # Si el usuario ingresa un mensaje de error personalizado lo retorna,
        # de lo contrario retorna el mensaje predeterminado:
        if self.wrong_option_text:
            return self.wrong_option_text
        return 'La opción "{}" no es válida.'.format(user_input)

    def print_alternatives(self):
        # Muestra un listado numerado de todos los nombres de los objetos "Option" almacenados:
        count = 1
        print()
        for option in self.alternatives:
            print("\t[" + str(count) + "] " + str(
                option))  # El metodo str() sobre el objeto "Option" retorna su nombre (ver linea 21)
            count += 1
        print()

    def execute_function(self, selection):
        # Toma un "input" que se sabe es sólo numérico y ejecuta la opción asociada.
        # Si el número está fuera de rango, muestra el mensaje de error y retorna "False"
        # Posee varios "print()" para mejorar el fomrato y legibilidad de la consola.
        if int(selection) in range(1, len(self.alternatives) + 1):
            print('\n' + '-' * 40 + '\n')
            self.alternatives[int(selection) - 1].execute()
            print('\n' + '-' * 40 + '\n')
            return True
        else:
            print('\n' + self.set_wrong_input_mesage(selection) + '\n' + '-' * 40 + '\n')
            return False

    def catch_user_selection(self):
        # Este es el método encargado de pocesar los "input" del usuario.
        # Procesa que sean números y acepta varios si se definió como "True" la variable "multi_selection"
        selection = input(self.input_message)
        # Una opcion y es numérica:
        if selection.isnumeric() and not self.multi_selection:
            self.finish = self.execute_function(selection)
        # Si pueden ser varias opciones:
        elif self.multi_selection:
            values = []
            num_list = selection.split(',')
            for num in num_list:
                num = num.strip()
                if num.isnumeric():
                    values.append(self.execute_function(num))
                else:
                    print('\n' + self.set_wrong_input_mesage(selection) + '\n' + '-' * 40 + '\n')
            # Revisa si TODOS los inputs ingresados se encontraban dentro del rango de opciones:
            if sum(values) == len(num_list):
                self.finish = True
        else:
            print('\n' + self.set_wrong_input_mesage(selection) + '\n' + '-' * 40 + '\n')

    def show(self):
        # Ciclo principal del menú:
        while not self.finish:
            print(self.user_info)
            self.print_alternatives()
            self.catch_user_selection()
        self.finish = False


if __name__ == '__main__':
    def print_text(text, text2):
        print(text)
        print(text2)


    menu_usuario = Menu()
    menu_usuario.add('Saludo y Despedida', print_text, 'holahola', 'chaochoa')
    menu_usuario.add('Risas', print_text, 'jajjajjaja', 'jejejjeje')
    menu_usuario.add('Frutas', print_text, 'manzana', 'platano')
    # menu_usuario.show()

    segundo_menu = Menu(multi_selection=True, user_info='ELIGE RÁAAAAAAAPIDO',
                        wrong_option_text='Nop, esa opcion no sirve')
    segundo_menu.add('Animales', print_text, 'vaca', 'caballo')
    segundo_menu.add('Marcas', print_text, 'Audi', 'Mercedez Benz')
    segundo_menu.add('Computadores', print_text, 'Acer', 'Asus')
    segundo_menu.add('Lápices', print_text, 'pasta', 'grafito')
    segundo_menu.show()
