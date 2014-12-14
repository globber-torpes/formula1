from unittest import TestCase
from src.Piloto import Piloto
from src.Escuderia import Escuderia
from src.CampeonatoMundial import CampeonatoMundial
from src.Circuito import Circuito
from src.GranPremio import GranPremio
from src.Formula1 import Formula1
from mockito import *

__author__ = 'MAMISHO'


class TestFormula1(TestCase):
    """
    Test Formula 1

    Este test prueba las funcionalidades del modulo de Formula1. Para
    realizar las mismas, es necesario tener una bateria de atributos
    definidos para todas las pruebas.

    :param p1: Piloto de prueba
    :param p2: Piloto de prueba
    :param p3: Piloto de prueba
    :param p4: Piloto de prueba
    :param p5: Piloto de prueba
    :param p6: Piloto de prueba
    :param e1: Escuderia de prueba
    :param e2: Escuderia de prueba
    :param e3: Escuderia de prueba
    """
    p1 = Piloto("AAA", "Piloto A")
    p2 = Piloto("BBB", "Piloto B")
    p3 = Piloto("CCC", "Piloto C")
    p4 = Piloto("DDD", "Piloto D")
    p5 = Piloto("EEE", "Piloto E")
    p6 = Piloto("FFF", "Piloto F")
    e1 = Escuderia("Escuderia 1")
    e2 = Escuderia("Escuderia 2")
    e3 = Escuderia("Escuderia 3")

    e1.agregar_piloto(p1)
    e1.agregar_piloto(p2)
    e2.agregar_piloto(p3)
    e2.agregar_piloto(p4)
    e3.agregar_piloto(p5)
    e3.agregar_piloto(p6)

    def test_crear_campeonato_mundial(self):
        """
        Test Crear un campeonato mundial

        El test comprueba que formula 1 pueda crear un
        campeonato mundial de forma correcta, para esto
        se comparan dos clases CampeonatoMundial, el primero lo creamos de
        forma manual y el segundo es el que creara el modulo de formula1.
        Luego comparamos las clases que tienen sus mismo atributos.

        :param f1: Formula 1 que va a crear el campeonato mundial
        :param es: Diccionario de escuderias necesario para construir un campeonato mundial
        :param cm1: Campeonato mundial creado de forma manual
        :param cm2: Campeonato mundial creado por formula 1
        """
        print("\ntest_crear_campeonato_mundial")
        f1 = Formula1()
        es = {self.e1.nombre: self.e1,
              self.e2.nombre: self.e2,
              self.e3.nombre: self.e3}
        cm1 = CampeonatoMundial(1, es)
        cm2 = f1.crear_campeonato_mundial(1, es)
        self.assertEqual(cm1.__class__, cm2.__class__)

    def test_agregar_campeonato_mundial_1(self):
        """
        Test agregar campeonato mundial a Formula 1

        Este test comprueba que un campeonato mundial sea
        agregado correctamente en la formula 1 cumpliendo
        con el esquema de datos requerido

        :param f1: Formula 1 al que se agrega el campeonat mundial
        :param es: Diccionario de escuderias que se requiere para crear un campeonato mundial
        :param cm: campeonato mundial que se agrega a la formula 1
        """
        print ("\ntest_agregar_campeonato_mundial_1")
        f1 = Formula1()
        es = {self.e1.nombre: self.e1,
              self.e2.nombre: self.e2,
              self.e3.nombre: self.e3}

        cm = CampeonatoMundial(1, es)
        self.assertEqual(f1.agregar_campeonato_mundial(cm), True)

    def test_agregar_campeonato_mundial_2(self):
        """
        Test agregar campeonato mundial repetido

        Este test comprueba que no pueda se agregado un
        campeonato mundial que ya existe en la formula 1. La prueba se va a realizar con
        un solo campeonato mundial en este caso cm. Se invoca dos veces a el metodo
        agregar_campeonato_mundial con el mismo parametro.

        :param f1: Formula1 al que se agrega el campeonato mundial
        :param es: Diccionario de escuderias que se requiere para crear un campeonato mundial
        :param cm: Campeonato mundial que se agrega a la formula 1
        """
        print ("\ntest_agregar_campeonato_mundial_2")
        f1 = Formula1()
        es = {self.e1.nombre: self.e1,
              self.e2.nombre: self.e2,
              self.e3.nombre: self.e3}

        cm = CampeonatoMundial(1, es)
        f1.agregar_campeonato_mundial(cm)
        self.assertEqual(f1.agregar_campeonato_mundial(cm), False)

    def test_agregar_campeonato_mundial_3(self):
        """
        Test agregar campeonato mundial invalido

        Este metodo comprueba que el nuevo campeonato mundial
        sea correcto, es decir que cumpla con los requerimientos
        de un campeonato mundial. En esta prueba vamos a simular un
        campeonato mundial, el cual no debe pasar la prueba porque, aunque
        sea simulado, no es un campeonato mundial.

        :param f1: Formula1 al que se agrega el campeonato mundial
        :param cm: mock que simula un campeonato mundial.
        """
        print ("\ntest_agregar_campeonato_mundial_3")
        f1 = Formula1()
        cm = mock(CampeonatoMundial)
        self.assertEqual(f1.agregar_campeonato_mundial(cm), False)

    def test_eliminar_campeonato_mundial_1(self):
        """
        Test eliminar campeonato mundial existente

        Este test comprueba que un campeonato mundial existente y que cumple
        con los requisitos sea eliminado de la formula 1.

        :param f1: formula 1 de donde se elimina el campeonato mundial
        :param es: Escuderia de prueba para crear campeonatos mundiales
        :param cm1: Campeoanto mundial de prueba
        :param cm2: Campeoanto mundial de prueba
        :param cm3: Campeoanto mundial de prueba
        :param cm4: Campeoanto mundial de prueba
        :param cm5: Campeoanto mundial de prueba
        """
        print("\ntest_eliminar_campeonato_mundial_1")
        f1 = Formula1()
        es = {self.e1.nombre: self.e1,
              self.e2.nombre: self.e2,
              self.e3.nombre: self.e3}
        cm1 = CampeonatoMundial(1, es)
        cm2 = CampeonatoMundial(2, es)
        cm3 = CampeonatoMundial(3, es)
        cm4 = CampeonatoMundial(4, es)
        cm5 = CampeonatoMundial(5, es)

        f1.agregar_campeonato_mundial(cm1)
        f1.agregar_campeonato_mundial(cm2)
        f1.agregar_campeonato_mundial(cm3)
        f1.agregar_campeonato_mundial(cm4)
        f1.agregar_campeonato_mundial(cm5)

        self.assertEqual(f1.eliminar_campeonato_mundial(cm1), True)

    def test_eliminar_campeonato_mundial_2(self):
        """
        Test eliminar campeonato mundial No existente

        Este test comprueba que un campeonato mundial debe
        existir para ser pasado como parametro y ser eliminado de
        la formula 1

        :param f1: formula 1 de donde se elimina el campeonato mundial
        :param es: Escuderia de prueba para crear campeonatos mundiales
        :param cm1: Campeoanto mundial No existente en la formula 1
        :param cm2: Campeoanto mundial existente en f1
        :param cm3: Campeoanto mundial existente en f1
        :param cm4: Campeoanto mundial existente en f1
        :param cm5: Campeoanto mundial existente en f1
        """
        print("\ntest_eliminar_campeonato_mundial_2")
        f1 = Formula1()
        es = {self.e1.nombre: self.e1,
              self.e2.nombre: self.e2,
              self.e3.nombre: self.e3}
        cm1 = CampeonatoMundial(1, es)
        cm2 = CampeonatoMundial(2, es)
        cm3 = CampeonatoMundial(3, es)
        cm4 = CampeonatoMundial(4, es)
        cm5 = CampeonatoMundial(5, es)

        f1.agregar_campeonato_mundial(cm2)
        f1.agregar_campeonato_mundial(cm3)
        f1.agregar_campeonato_mundial(cm4)
        f1.agregar_campeonato_mundial(cm5)

        self.assertEqual(f1.eliminar_campeonato_mundial(cm1), False)

    def test_eliminar_campeonato_mundial_3(self):
        """
        Test eliminar campeonato mundial no valido

        Este test comprueba que el campeonato mundial que
        va a ser eliminado, sea un campeonato mundial valido. Para este
        test usaremos un mock de tipo campeonato Mundial y la formula 1
        no debe permitir agregarlo porque, aunque sea simulado, no
        es un objeto propio de CampeonatoMundial

        :param f1: Formula 1 de donde se va a eliminar el campeonato mundial
        :param es: Diccionario de escuderias para crear los campeonatos mundiales
        :param cm1: Campeonato mundial de f1
        :param cm2: Campeonato mundial de f1
        :param cm3: mock que simula un campeonato mundial
        """
        print("\ntest_eliminar_campeonato_mundial_3")
        f1 = Formula1()
        es = {self.e1.nombre: self.e1,
              self.e2.nombre: self.e2,
              self.e3.nombre: self.e3}
        cm1 = CampeonatoMundial(1, es)
        cm2 = CampeonatoMundial(2, es)
        cm3 = mock(CampeonatoMundial)

        f1.agregar_campeonato_mundial(cm1)
        f1.agregar_campeonato_mundial(cm2)

        self.assertEqual(f1.eliminar_campeonato_mundial(cm3), False)
