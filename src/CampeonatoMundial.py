import operator
import Error
from GranPremio import GranPremio


class CampeonatoMundial():

    def __init__(self, edicion, escuderias):
        """
        Constructor Campeonato Mundial comprobando que el parametro edicion es de tipo int y
        escuderia de tipo diccionario

        """
        if isinstance(edicion, int) and isinstance(escuderias, dict):
            self.edicion = edicion
            self.escuderias = escuderias
            self.grandesPremios = {}
            self.rankingPilotos = {}
            self.rankingEscuderias = {}
        else:
            Error.TipoException("edicion/escuderia")

    def agregargranpremio(self, granpremio):
        """
        Comprueba que granpremio es una instancia de gran premio y si lo es la anade

        :param granpremio: instancia de gran premio
        """
        if isinstance(granpremio, GranPremio) and (granpremio not in self.grandesPremios):
            self.grandesPremios[granpremio.nombre] = granpremio
        else:
            print "Error al agregar el Gran Premio al Campeonato Mundial edicion " + str(self.edicion) + "."

    def eliminargranpremio(self, granpremio):
        """
        Comprueba que granpremio es una instancia de gran premio y si lo es la elimina

        :param granpremio: instancia de gran premio
        """
        if isinstance(granpremio, GranPremio) and (granpremio in self.grandesPremios):
            del self.grandesPremios[granpremio.nombre]
        else:
            print "Error al eliminar el Gran Premio del Campeonato Mundial edicion " + str(self.edicion) + "."

    def creargranpremio(self, nombre, circuito, pais=None, fecha=None):
        """
        Crea un gran premio con los parametros pasados

        :return: devuelve instancia gran premio
        :rtype Gran premio
        """
        gp = GranPremio(nombre, circuito, self.escuderias, pais, fecha)
        self.agregargranpremio(gp)
        return gp

    def printgrandesgremios(self):
        """
        imprime todos los grandes premios existentes

        """
        for gp in self.grandesPremios.values():
            print gp

    def actualizarrankings(self, granpremio):
        """
        Comprueba que gran premio es una instancia de gran premio, si lo es suma la puntuaciones de pilotos y
        escuderias para actualizar las listas

        :param granpremio: instancia de gran premio
        """
        if isinstance(granpremio, GranPremio) and not granpremio.puntuacionFinal == []:
            for piloto in granpremio.puntuacionFinal[0].keys():
                if piloto in self.rankingPilotos:
                    self.rankingPilotos[piloto] += granpremio.puntuacionFinal[0][piloto]
                else:
                    self.rankingPilotos[piloto] = granpremio.puntuacionFinal[0][piloto]
            for escuderia in granpremio.puntuacionFinal[1].keys():
                if escuderia in self.rankingEscuderias:
                    self.rankingEscuderias[escuderia] += granpremio.puntuacionFinal[1][escuderia]
                else:
                    self.rankingEscuderias[escuderia] = granpremio.puntuacionFinal[1][escuderia]
        else:
            print "Error al actualizar ranking."

    def simulargranpremio(self, granpremio):
        """
        Comprueba si el gran premio existe, si existe anade clasificacion la imprime y actualiza los rankings

        :param granpremio: instancia de gran premio
        """
        if granpremio.nombre in self.grandesPremios:
            granpremio.setClasificacion()
            granpremio.printClasificacion()
            self.actualizarrankings(granpremio)
        else:
            print "Error. El gran premio no se encuentra registrado dentro de este Campeonato Mundial"

    def printrankingpilotos(self, imprimir=True):
        """
        Imprime la tabla e ranking de pilotos con sus puntuaciones

        :return:ranking de pilotos
        :rtype: string
        """
        tostring = "Ranking de pilotos del Campeonato Mundial de F1 (Edicion " + str(self.edicion) + ")"
        sorted_rankingpilotos = sorted(self.rankingPilotos.items(), key=operator.itemgetter(1), reverse=True)
        for piloto in sorted_rankingpilotos:
            tostring += "\n\t" + piloto[0] + " -> " + str(piloto[1])
        if imprimir:
            print tostring + "\n"
        return tostring

    def printrankingescuderias(self, imprimir=True):
        """
        Imprime el ranking de escuderias

        :return: ranking escuderias
        :rtype: string
        """
        tostring = "Ranking de escuderias del Campeonato Mundial de F1 (Edicion " + str(self.edicion) + ")"
        sorted_rankingescuderias = sorted(self.rankingEscuderias.items(), key=operator.itemgetter(1), reverse=True)
        for escuderia in sorted_rankingescuderias:
            tostring += "\n\t" + escuderia[0] + " -> " + str(escuderia[1])
        if imprimir:
            print tostring + "\n"
        return tostring

    def __str__(self):
        """
        Metodo tostring

        Devuelve los datos del campeontao mundial, escuderias, grandes premios, ranking de pilotos y escuderias

        :return: cadena con todos los datos
        :rtype: String
        """
        tostring = "Campeonato Mundial de F1 edicion " + str(self.edicion) + ":"
        tostring += "\nEscuderias inscritas: " + str(self.escuderias.keys())
        tostring += "\nGrandes Premios: " + str(self.grandesPremios.keys())
        if self.rankingPilotos:
            tostring += "\n" + self.printrankingpilotos(False)
        if self.rankingEscuderias:
            tostring += "\n" + self.printrankingescuderias(False)
        return tostring + "\n"
