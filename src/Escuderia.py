from Piloto import Piloto


class Escuderia():
    """
    Modela una escuderia

    :author: Francisco Lopez Baena
    :version: 1
    """

    def __init__(self, nombre, sede=None, chasis=None, motor=None, neumaticos=None, p_temp=None, f_crea=None):
        """
        descripcion breve: constructor

        descripcion detallada: inicializador de la clase escuderia

        :param nombre: nombre de la escuderia
        :param sede: sede de la escuderia
        :param chasis: chasis de la escuderia
        :param motor: motor de la escuderia
        :param neumaticos: neumaticos que usa la escuderia
        :param p_temp: primera temporada de la escuderia
        :param f_crea: fecha de creacion de la escuderia
        :return: no devuelve nada
        """
        self.nombre = nombre
        self.sede = sede
        self.chasis = chasis
        self.motor = motor
        self.neumaticos = neumaticos
        self.primera_temp = p_temp
        self.fecha_crea = f_crea
        self.pilotos = {}
        self.pilotos_activos = {}

    def agregar_piloto(self, piloto):
        """
        descripcion breve: agregar piloto

        descripcion detallada: metodo para agregar piloto a la escuderia

        :param piloto: piloto
        :return: no devuelve nada
        """
        if isinstance(piloto, Piloto) and (piloto.id_piloto not in self.pilotos):
            piloto.equipo = self.nombre
            self.pilotos[piloto.id_piloto] = piloto
            if len(self.pilotos_activos) < 2 and piloto.id_piloto not in self.pilotos_activos:
                self.pilotos_activos[piloto.id_piloto] = piloto
        else:
            print "Error al agregar piloto a la escuderia " + self.nombre + "."

    def eliminar_piloto(self, piloto):
        """
        descripcion breve: eliminar piloto

        descripcion detallada: metodo para eliminar piloto de la escuderia

        :param piloto: piloto
        :return: no devuelve nada
        """
        if isinstance(piloto, Piloto) and (piloto.id_piloto in self.pilotos):
            piloto.equipo = None
            piloto.equipo_anterior = self.nombre
            del self.pilotos[piloto.id_piloto]
            if piloto.id_piloto in self.pilotos_activos:
                del self.pilotos_activos[piloto.id_piloto]
                if len(self.pilotos_activos) < 2:
                    print "Atencion, el piloto eliminado estaba marcado como activo. Redefina los pilotos activos."
        else:
            print "Error al eliminar piloto de la escuderia " + self.nombre + "."

    def definir_pilotos_activos(self, piloto1, piloto2):
        """
        descripcion breve: deifinir piloto

        descripcion detallada: metodo para definir los pilotos a la escuderia

        :param piloto1: piloto1
        :param piloto2: piloto2
        :return: no devuelve nada
        """
        if isinstance(piloto1, Piloto) and isinstance(piloto2, Piloto):
            self.pilotos_activos.clear()
            self.pilotos_activos[piloto1.id_piloto] = piloto1
            self.pilotos_activos[piloto2.id_piloto] = piloto2
        else:
            print "Error al definir pilotos activos de la escuderia " + self.nombre + "."

    def sustituir_piloto(self, piloto1, piloto2):
        """
        descripcion breve: sustituir piloto

        descripcion detallada: metodo para sustituir piloto en la escuderia

        :param piloto1: piloto1
        :param piloto2: piloto2
        :return: no devuelve nada
        """
        if isinstance(piloto1, Piloto) and isinstance(piloto2, Piloto):
            if piloto1.id_piloto in self.pilotos_activos.keys():
                del self.pilotos_activos[piloto1.id_piloto]
                self.pilotos_activos[piloto2.id_piloto] = piloto2
            self.eliminar_piloto(piloto1)
            self.agregar_piloto(piloto2)
        else:
            print "Error al sustituir pilotos en la escuderia " + self.nombre + "."

    def __str__(self):
        """
        descripcion breve: imprimir

        descripcion detallada: metodo para mostrar(imprimir) los datos de escuderia

        :return: no devuelve nada
        """
        tostring = "Datos de la Escuderia: \nNombre de la escuderia: " + str(self.nombre)
        if self.sede:
            tostring += "\nUbicacion de la sede: " + self.sede
        if self.chasis:
            tostring += "\nChasis utilizado: " + self.chasis
        if self.motor:
            tostring += "\nMotor montado: " + self.motor
        if self.neumaticos:
            tostring += "\nMarca de neumaticos: " + self.neumaticos
        if self.primera_temp:
            tostring += "\nPrimera temporada?: " + str(self.primera_temp)
        if self.fecha_crea:
            tostring += "\nFecha de creacion de la Escuderia: " + str(self.fecha_crea)
        if self.pilotos:
            tostring += "\nPilotos en plantilla: \n\t" + str(self.pilotos.keys())
        if self.pilotos_activos:
            tostring += "\nPilotos activos: \n\t" + str(self.pilotos_activos.keys())
        return tostring + "\n"