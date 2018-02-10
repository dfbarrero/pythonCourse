class ClaseP:
    def __init__(self, name):
        self.__name = name
        print(name, ' , objeto creado')

    # metodo invocado cuando un objeto desaparece de memoria. Libera recursos: reservas de memoria, archivos abtos,
    # conexiones a bases de datos,...
    def __del__(self):
        print(self.__name, ' , objeto ya destruido')

# si se ejecuta solo esta linea, vereis que se crea el objeto y se destruye (al finalizar la ejecucion del script)
# aparecen los mensajes de __init__ y __del__, respectivamente
x = ClaseP('OBJETO 1')

z = ClaseP('OBJETO 3')

z = x

y = ClaseP('OBJETO 2')

del(x)

# el 'OBJETO 2' tambien se destruye al finalizar el script aunque no explícitamente con la invocación a del(y)