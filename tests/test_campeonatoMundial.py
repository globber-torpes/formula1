from unittest import TestCase
from src.GranPremio import *
from src.CampeonatoMundial import *
from src.Circuito import *
from src.Piloto import *
from src.Escuderia import *


__author__ = 'manolo'


class TestCampeonatoMundial(TestCase):
    def test_agregar_gran_premio(self):
        """
        Test agregar gran premio
        Este test coprueba que se agrega correctamente un gran premio a un campeonato mundial
        Vemos el caso de exito

        """
        e1 = Escuderia("Ferrari", "Maranello")
        e2 = Escuderia("Red Bull")

        es = {e1.nombre: e1, e2.nombre: e2}

        p1 = Piloto("ALO", "Fernando", "Alonso", "Ferrari")
        p2 = Piloto("MAS", "Felipe", "Massa", "Ferrari")
        p3 = Piloto("WEB", "Mark", "Webber", "Red Bull")
        p4 = Piloto("VET", "Sebastien", "Vettel", "Red Bull")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e2.agregar_piloto(p3)
        e2.agregar_piloto(p4)

        c1 = Circuito("Red Bull Ring", "Spielberg", 4326)
        c2 = Circuito("Circuito de Sochi", "Sochi")

        gp1 = GranPremio("Gran Premio 1", c1, es, "USA", "2014")

        cm = CampeonatoMundial(2014, es)

        self.assertEqual(cm.agregar_gran_premio(gp1), True)

    def test_agregargranpremio_failure(self):
        """
        Test agregar gran premio
        Este test coprueba que solo permite agregar gandes premios de tipo grandes premios
        Vemos el caso de falla

        """
        e1 = Escuderia("Ferrari", "Maranello")
        e2 = Escuderia("Red Bull")

        es = {e1.nombre: e1, e2.nombre: e2}

        p1 = Piloto("ALO", "Fernando", "Alonso", "Ferrari")
        p2 = Piloto("MAS", "Felipe", "Massa", "Ferrari")
        p3 = Piloto("WEB", "Mark", "Webber", "Red Bull")
        p4 = Piloto("VET", "Sebastien", "Vettel", "Red Bull")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e2.agregar_piloto(p3)
        e2.agregar_piloto(p4)

        c1 = Circuito("Red Bull Ring", "Spielberg", 4326)

        cm = CampeonatoMundial(2014, es)

        self.assertEqual(cm.agregar_gran_premio(c1), False)

    def test_actualizar_rankings(self):
        """
        Test de actualizar rankings
        Comprobamos que al pasarle la puntuacion equivalente a una clasificacion, este suma dichos puntos
        a sus correspondientes pilotos y escuderias
        Comprobamos caso de exito

        """
        e1 = Escuderia("Ferrari", "Maranello")
        e2 = Escuderia("Red Bull")

        es = {e1.nombre: e1, e2.nombre: e2}

        p1 = Piloto("ALO", "Fernando", "Alonso", "Ferrari")
        p2 = Piloto("MAS", "Felipe", "Massa", "Ferrari")
        p3 = Piloto("WEB", "Mark", "Webber", "Red Bull")
        p4 = Piloto("VET", "Sebastien", "Vettel", "Red Bull")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e2.agregar_piloto(p3)
        e2.agregar_piloto(p4)

        c1 = Circuito("Red Bull Ring", "Spielberg", 4326)
        c2 = Circuito("Circuito de Sochi", "Sochi")

        gp1 = GranPremio("Gran Premio 1", c1, es, "USA", "2014")
        gp1.puntuacionFinal = [{'WEB': 18, 'VET': 15, 'MAS': 12, 'ALO': 25}, {'Red Bull': 33, 'Ferrari': 37}]
        cm = CampeonatoMundial(2014, es)
        self.assertEqual(cm.actualizar_rankings(gp1), True)

    def test_actualizar_rankings_failure(self):
        """
        Test de actualizar ranking
        Comprobamos que al pasarle una puntuacion final vacia , da fallo el recalcular los puntos de
        los pilotos y escuderias
        :return:
        """
        e1 = Escuderia("Ferrari", "Maranello")
        e2 = Escuderia("Red Bull")

        es = {e1.nombre: e1, e2.nombre: e2}

        p1 = Piloto("ALO", "Fernando", "Alonso", "Ferrari")
        p2 = Piloto("MAS", "Felipe", "Massa", "Ferrari")
        p3 = Piloto("WEB", "Mark", "Webber", "Red Bull")
        p4 = Piloto("VET", "Sebastien", "Vettel", "Red Bull")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e2.agregar_piloto(p3)
        e2.agregar_piloto(p4)

        c1 = Circuito("Red Bull Ring", "Spielberg", 4326)
        c2 = Circuito("Circuito de Sochi", "Sochi")

        gp1 = GranPremio("Gran Premio 1", c1, es, "USA", "2014")
        gp1.puntuacionFinal = []
        cm = CampeonatoMundial(2014, es)
        self.assertEqual(cm.actualizar_rankings(gp1), False)