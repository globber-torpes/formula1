import Error
import re
from Circuito import Circuito

class GranPremio():
    puntuaciones = {1:25, 2:18, 3:15, 4:12, 5:10, 6:8, 7:6, 8:4, 9:2, 10:1}

    def __init__(self, nombre, circuito, escuderias, pais = None, fecha = None):
        if(isinstance(circuito, Circuito)):
            self.nombre = nombre
            self.pais = pais
            self.fecha = fecha
            self.circuito = circuito
            self.participantes = {}
            self.clasificacion = {}
            self.puntuacionFinal = []
            self.vueltaRapida = {}
            self.extraerParticipantes(escuderias)
        else:
            raise Error.TipoException("circuito")


    def extraerParticipantes(self,escuderias):
        # participantes = ["ALO":{"Piloto":"Alonso", "Escuderia":"Ferrari"},"VET":{"Piloto":"Vettel", "Escuderia":"Red Bull"}]
        for escuderia in escuderias.values():
            if(len(escuderia.pilotosActivos) == 2):
                for piloto in escuderia.pilotosActivos.keys():
                    self.participantes[escuderia.pilotosActivos[piloto].idPiloto] = {"Piloto":escuderia.pilotosActivos[piloto].idPiloto, "Escuderia":escuderia.nombre}
            else:
                raise Error.ActivosException(escuderia.nombre)

    def setClasificacion(self):
        # clasificacion = {1:{"Piloto":"Alonso", "Escuderia":"Ferrari"},2:{"Piloto":"Vettel", "Escuderia":"Red Bull"}}
        # puntuacionesPilotos = {"Alonso":25, "Vettel":18}
        # puntuacionesEscuderias = {"Ferrari":25, "Red Bull": 18}

        puntuacionesPilotos = {}
        puntuacionesEscuderias = {}

        print "Editor de clasificaciones."
        print "Se mostraran los participantes por pantalla. Introduzca la posicion para cada piloto:"
        
        for piloto in self.participantes.values():
            print "Piloto: " + piloto["Piloto"] +". Escuderia: " + piloto["Escuderia"]
            pos = input()
            while not isinstance(pos,int) or pos>len(self.participantes) or pos<1 or pos in self.clasificacion.keys():
                print "Error. Posicion repetida o no admitida."
                pos = input()
            self.clasificacion[pos] = piloto
            if (pos in self.puntuaciones):
                puntuacionesPilotos[piloto["Piloto"]] = self.puntuaciones[pos]
                if piloto["Escuderia"] in puntuacionesEscuderias:
                    puntuacionesEscuderias[piloto["Escuderia"]] += self.puntuaciones[pos]
                else:
                    puntuacionesEscuderias[piloto["Escuderia"]] = self.puntuaciones[pos]
            else:
                puntuacionesPilotos[piloto["Piloto"]] = 0
                if (piloto["Escuderia"] not in puntuacionesEscuderias):
                    puntuacionesEscuderias[piloto["Escuderia"]] = 0
        print "Desea ahora definir la vuelta rapida? (s/n). Recuerde introducir la respuesta entre comillas:"
        res = str(input())
        while not isinstance(res,str) or res is not "s" and  res is not "n":
            print "Error. Respuesta no valida."
            res = str(input())
        if(res == "s"):
            print "Introduzca el codigo de piloto que ha realizado la vuelta rapida. Recuerde introducir la respuesta entre comillas:"
            p = str(input())
            while p not in self.participantes.keys():
                print "Error. Piloto no encontrado."
                p = str(input())
            print "Introduzca el tiempo de la vuelta rapida. Formato recomendado '1:16.182'. Recuerde introducir la respuesta entre comillas:"
            t = str(input())
            regex = re.compile("([0-9]+:[0-6][0-9].[0-9][0-9][0-9])")
            r = regex.search(t)
            while r is None:
                print "Error. Formato de tiempo incorrecto"
                t = str(input())
                r = regex.search(t)
            self.setVueltaRapida(t,p)
        self.puntuacionFinal = [puntuacionesPilotos, puntuacionesEscuderias]

    def printClasificacion(self, imprimir = True):
        strclasificacion = "Clasificacion "+ self.nombre +":"
        for piloto in self.clasificacion.keys():
            strclasificacion += "\n\t" + str(piloto) + " -> " + self.clasificacion[piloto]["Piloto"] + " (" + self.clasificacion[piloto]["Escuderia"] + ")"
        if imprimir:
            print strclasificacion + "\n"
        return strclasificacion

    def printParticipantes(self, imprimir = True):
        strparticipantes = "Lista de participantes "+ self.nombre +":"
        for piloto in self.participantes.keys():
            strparticipantes += "\n\tPiloto: " + self.participantes[piloto]["Piloto"] + ". Escuderia: " + self.participantes[piloto]["Escuderia"]
        if imprimir:
            print strparticipantes
        return strparticipantes

    def setVueltaRapida(self, tiempo, piloto = None):
        if (piloto in self.participantes.keys()):
            self.vueltaRapida = {"Tiempo": tiempo, "Piloto": piloto}
        else:
            self.vueltaRapida = {"Tiempo": tiempo}

    def printVueltaRapida(self, imprimir = True):
        vueltaRapidaString = "Vuelta rapida "+ self.nombre +":\n\tTiempo: " + self.vueltaRapida["Tiempo"]
        if self.vueltaRapida["Piloto"]:
            vueltaRapidaString += "\n\tPiloto: " + self.vueltaRapida["Piloto"]
        if imprimir:
            print vueltaRapidaString
        return vueltaRapidaString

    def __str__(self):
        tostring = "Datos del Gran Premio: \nNombre: " + str(self.nombre)
        if(self.pais != None):
            tostring += "\nPais: " + self.pais
        if(self.fecha != None):
            tostring += "\nFecha de celebracion: " + self.fecha
        if(self.circuito != None):
            tostring += "\nCircuito: " + self.circuito.nombre
        if(self.clasificacion):
            tostring += "\n" + self.printClasificacion(False)
            if(self.vueltaRapida):
                tostring += "\n" + self.printVueltaRapida(False)
        else:
            if(self.participantes):
                tostring += "\n" + self.printParticipantes(False)
        return tostring + "\n"
