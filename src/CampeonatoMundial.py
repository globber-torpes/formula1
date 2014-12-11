import operator
import Error
from GranPremio import GranPremio

class CampeonatoMundial():

    def __init__(self, edicion, escuderias):
        """
        Constructor Campeonato Mundial comprobando que el parametro edicion es de tipo int y escuderia de tipo diccionario
        """
        if(isinstance(edicion, int) and isinstance(escuderias, dict)):
            self.edicion = edicion
            self.escuderias = escuderias
            self.grandesPremios = {}
            self.rankingPilotos = {}
            self.rankingEscuderias = {}
        else:
            Error.TipoException("edicion/escuderia")

    def agregarGranPremio(self, granPremio):
        """
        Comprueba que granpremio es una instancia de gran premio y si lo es la anade

        :param granPremio: instancia de gran premio
        """
        if (isinstance(granPremio, GranPremio) and (granPremio not in self.grandesPremios)):
            self.grandesPremios[granPremio.nombre] = granPremio
        else:
            print "Error al agregar el Gran Premio al Campeonato Mundial edicion " + str(self.edicion) + "."

    def eliminarGranPremio(self, granPremio):
        """
        Comprueba que granpremio es una instancia de gran premio y si lo es la elimina

        :param granPremio: instancia de gran premio
        """
        if (isinstance(granPremio, GranPremio) and (granPremio in self.grandesPremios)):
            del self.grandesPremios[granPremio.nombre]
        else:
            print "Error al eliminar el Gran Premio del Campeonato Mundial edicion " + str(self.edicion) + "."

    def crearGranPremio(self, nombre, circuito, pais = None, fecha = None):
        """
        Crea un gran premio con los parametros pasados

        :return: devuelve instancia gran premio
        :rtype Gran premio
        """
        gp = GranPremio(nombre,circuito,self.escuderias,pais,fecha)
        self.agregarGranPremio(gp)
        return gp

    def printGrandesPremios(self):
        """
        imprime todos los grandes premios existentes

        """
        for gp in self.grandesPremios.values():
            print gp

    def actualizarRankings(self, granPremio):
        """
        Comprueba que gran premio es una instancia de gran premio, si lo es suma la puntuaciones de pilotos y
        escuderias para actualizar las listas

        :param granPremio: instancia de gran premio
        """
        if (isinstance(granPremio, GranPremio) and  not granPremio.puntuacionFinal == []):
            for piloto in granPremio.puntuacionFinal[0].keys():
                if(piloto in self.rankingPilotos):
                    self.rankingPilotos[piloto] += granPremio.puntuacionFinal[0][piloto]
                else:
                    self.rankingPilotos[piloto] = granPremio.puntuacionFinal[0][piloto]
            for escuderia in granPremio.puntuacionFinal[1].keys():
                if(escuderia in self.rankingEscuderias):
                    self.rankingEscuderias[escuderia] += granPremio.puntuacionFinal[1][escuderia]
                else:
                    self.rankingEscuderias[escuderia] = granPremio.puntuacionFinal[1][escuderia]
        else:
            print "Error al actualizar ranking."

    def simularGranPremio(self, granPremio):
        """
        Comprueba si el gran premio existe, si existe anade clasificacion la imprime y actualiza los rankings

        :param granPremio: instancia de gran premio
        """
        if granPremio.nombre in self.grandesPremios:
            granPremio.setClasificacion()
            granPremio.printClasificacion()
            self.actualizarRankings(granPremio)
        else:
            print "Error. El gran premio no se encuentra registrado dentro de este Campeonato Mundial"

    def printRankingPilotos(self, imprimir = True):
        """
        Imprime la tabla e ranking de pilotos con sus puntuaciones

        :return:ranking de pilotos
        :rtype: string
        """
        toString = "Ranking de pilotos del Campeonato Mundial de F1 (Edicion " + str(self.edicion) + ")"
        sorted_rankingPilotos = sorted(self.rankingPilotos.items(), key=operator.itemgetter(1), reverse=True)
        for piloto in sorted_rankingPilotos:
            toString += "\n\t" + piloto[0] + " -> " + str(piloto[1])
        if imprimir:
            print toString + "\n"
        return toString

    def printRankingEscuderias(self, imprimir = True):
        """
        Imprime el ranking de escuderias

        :return: ranking escuderias
        :rtype: string
        """
        toString = "Ranking de escuderias del Campeonato Mundial de F1 (Edicion " + str(self.edicion) + ")"
        sorted_rankingEscuderias = sorted(self.rankingEscuderias.items(), key=operator.itemgetter(1), reverse=True)
        for escuderia in sorted_rankingEscuderias:
            toString += "\n\t" + escuderia[0] + " -> " + str(escuderia[1])
        if imprimir:
            print toString + "\n"
        return toString

    def __str__(self):
        """
        Metodo tostring

        Devuelve los datos del campeontao mundial, escuderias, grandes premios, ranking de pilotos y escuderias

        :return: cadena con todos los datos
        :rtype: String
        """
        toString = "Campeonato Mundial de F1 edicion " + str(self.edicion) + ":"
        toString += "\nEscuderias inscritas: " + str(self.escuderias.keys())
        toString += "\nGrandes Premios: " + str(self.grandesPremios.keys())
        if self.rankingPilotos:
            toString += "\n" + self.printRankingPilotos(False)
        if self.rankingEscuderias:
            toString += "\n" + self.printRankingEscuderias(False)
        return toString + "\n"
