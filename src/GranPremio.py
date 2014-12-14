import Error
import re
from src.Circuito import Circuito


class GranPremio(object):
    puntuaciones = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}

    def __init__(self, nombre, circuito, escuderias, pais, fecha):
        """
        Clase GranPremio

        Esta clase contiene el circuito, escuderias, pais y fecha donde se va a realizar
        el gran premio, este objeto posterioemente sera utilizado por un campeonato
        mundial y agregado a la formula 1. Para que el granPremio sea creado de forma correcta
        se comprueba la coherencia de los datos.

        :param nombre:  Nombre del gran premio
        :param circuito: Circuito en el que se realiza la competicion
        :param escuderias: Diccionario de escuderias que participan en el Gran premio
        :param pais: Pais donde se realiza el Gran Premio
        :param fecha: Fecha de la competicion
        """

        if isinstance(circuito, Circuito):
            self.nombre = nombre
            self.pais = pais
            self.fecha = fecha
            self.circuito = circuito
            self.participantes = {}
            self.clasificacion = {}
            self.puntuacionFinal = []
            self.vueltaRapida = {}
            self.extraer_participantes(escuderias)
        else:
            raise Error.TipoException("circuito")

    def extraer_participantes(self, escuderias):
        """
        Extraer Participantes

        Metodo que cumple la funcionalidad de devolver los participantes
        del diccionario de  escuderias que son pasadas por paramentro. Para
        su buen funcionamiento se comprueba la coherencia de los datos.

        :param escuderias: Diccionario de escuderias de donde se extraeran los participantes
        :return participantes: Diccionario con los participantes de las escuderias
        """
        for escuderia in escuderias.values():
            if len(escuderia.pilotosActivos) == 2:
                for piloto in escuderia.pilotosActivos.keys():
                    self.participantes[escuderia.pilotosActivos[piloto].idPiloto] = {
                        "Piloto": escuderia.pilotosActivos[piloto].idPiloto, "Escuderia": escuderia.nombre}
            else:
                raise Error.ActivosException(escuderia.nombre)
        return self.participantes

    def set_clasificacion(self):
        """
        Set Clasificacion

        Este metodo permite recoger los datos introdicidos por un usuario
        y validarlos. los datos introducidos por el usuario son las posiciones
        de los participantes, tambien se pude introcudir el tiempo de la vuelta
        rapida de un participante. lso datos se gusrdaran en diccionarios de la clase.

        :param puntuaciones_pilotos: Diccionario donde se agregan los pilotos
        :param puntuaciones_escuderias: Diccionario donde se agregan las escuerias.
        """
        puntuaciones_pilotos = {}
        puntuaciones_escuderias = {}

        print("Editor de clasificaciones.")
        print("Se mostraran los participantes por pantalla. Introduzca la posicion para cada piloto:")

        for piloto in self.participantes.values():
            print("Piloto: " + piloto["Piloto"] + ". Escuderia: " + piloto["Escuderia"])
            pos = input()
            while not isinstance(pos, int) or \
                            pos > len(self.participantes) or \
                            pos < 1 or \
                            pos in self.clasificacion.keys():
                print("Error. Posicion repetida o no admitida.")
                pos = input()
            self.clasificacion[pos] = piloto
            if pos in self.puntuaciones:
                puntuaciones_pilotos[piloto["Piloto"]] = self.puntuaciones[pos]
                if piloto["Escuderia"] in puntuaciones_escuderias:
                    puntuaciones_escuderias[piloto["Escuderia"]] += self.puntuaciones[pos]
                else:
                    puntuaciones_escuderias[piloto["Escuderia"]] = self.puntuaciones[pos]
            else:
                puntuaciones_pilotos[piloto["Piloto"]] = 0
                if piloto["Escuderia"] not in puntuaciones_escuderias:
                    puntuaciones_escuderias[piloto["Escuderia"]] = 0
        print("Desea ahora definir la vuelta rapida? (s/n).")

        res = str(raw_input())
        res = res.strip('\n')

        while res != "s" and res != "n":
            print("Error. Respuesta no valida.")
            res = str(raw_input())
            res = res.strip('\n')
        if res == "s":
            print("Introduzca el codigo de piloto que ha realizado la vuelta rapida.")
            p = str(raw_input())
            p = p.strip('\n')
            while p not in self.participantes.keys():
                print("Error. Piloto no encontrado.")
                p = str(raw_input())
                p = p.strip('\n')
            print("Introduzca el tiempo de la vuelta rapida. Formato recomendado '1:16.182'.")
            t = str(raw_input())
            t = t.strip('\n')
            regex = re.compile("([0-9]+:[0-6][0-9].[0-9][0-9][0-9])")
            r = regex.search(t)
            while r is None:
                print("Error. Formato de tiempo incorrecto")
                t = str(raw_input())
                t = t.strip('\n')
                r = regex.search(t)
            self.set_vuelta_rapida(t, p)
        self.puntuacionFinal = [puntuaciones_pilotos, puntuaciones_escuderias]

    def print_clasificacion(self, imprimir=True):
        """
        Print Clasificacion

        Muestra por pantalla la clasificiacion del gran premio.

        :param imprimir: Boolean que indica si imprimir o no el gran premio.
        :return strcclasificacion: String que se mostrara por pantalla
        """
        strclasificacion = "Clasificacion " + self.nombre + ":"
        for piloto in self.clasificacion.keys():
            strclasificacion += "\n\t" + str(piloto) + " -> " + self.clasificacion[piloto]["Piloto"] + " (" + \
                                self.clasificacion[piloto]["Escuderia"] + ")"
        if imprimir:
            print(strclasificacion + "\n")
        return strclasificacion

    def print_participantes(self, imprimir=True):
        """
        Print Participantes

        Muestra por pantalla los participantes del gran premio, los datos solo seran
        el nombre y la escuderia a la que pertenece

        :param imprimir: Boolean que indica si imprimir o no los datos
        :return:
        """
        strparticipantes = "Lista de participantes " + self.nombre + ":"
        for piloto in self.participantes.keys():
            strparticipantes += "\n\tPiloto: " + self.participantes[piloto]["Piloto"] + ". Escuderia: " + \
                                self.participantes[piloto]["Escuderia"]
        if imprimir:
            print(strparticipantes)
        return strparticipantes

    def set_vuelta_rapida(self, tiempo, piloto=None):
        """
        Set Vuelta Rapida

        El metodo permite indicar la vuelta rapida de un piloto.

        :param tiempo: String que indica el tiempo de la vuelta rapida
        :param piloto: Piloto que realiza la vuelta rapida
        :return True: si la vuelta rapida es agregada con exito
        :return False: si la vuelta rapida no es agregada
        """
        if piloto in self.participantes.keys():
            self.vueltaRapida = {"Tiempo": tiempo, "Piloto": piloto}
            return True
        else:
            self.vueltaRapida = {"Tiempo": tiempo}
            return False

    def print_vuelta_rapida(self, imprimir=True):
        """
        Print Vuelta Rapida

        El metodo permite la funcionalidad de mostras los datos de una vuelta
         rapida por pantalla devlviendo un String

        :param imprimir: Boolean que indica si se debe imprimir
        :return: String con los datos que se van a mostrar por pantalla
        """
        vuelta_rapida_string = "Vuelta rapida " + self.nombre + ":\n\tTiempo: " + self.vueltaRapida["Tiempo"]
        if self.vueltaRapida["Piloto"]:
            vuelta_rapida_string += "\n\tPiloto: " + self.vueltaRapida["Piloto"]
        if imprimir:
            print(vuelta_rapida_string)
        return vuelta_rapida_string

    def __str__(self):
        """
        Metodo privado ToString

        Se redefine el metodo toString para que muetre los datos
        del gran premio por pantalla siguiendo un estilo propio.

        :return: String que se mostrara por pantalla
        """
        tostring = "Datos del Gran Premio: \nNombre: " + str(self.nombre)
        if self.pais is not None:
            tostring += "\nPais: " + self.pais
        if self.fecha is not None:
            tostring += "\nFecha de celebracion: " + self.fecha
        if self.circuito is not None:
            tostring += "\nCircuito: " + self.circuito.nombre
        if self.clasificacion:
            tostring += "\n" + self.print_clasificacion(False)
            if self.vueltaRapida:
                tostring += "\n" + self.print_vuelta_rapida(False)
        else:
            if self.participantes:
                tostring += "\n" + self.print_participantes(False)
        return tostring + "\n"
