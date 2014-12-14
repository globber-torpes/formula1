from unittest import TestCase
from src.Piloto import *
from src.Escuderia import *
from mockito import *

__author__ = 'MAMISHO'


class TestEscuderia(TestCase):
    def test_agregar_piloto_1(self):
        """
        Test Agregar Piloto a Escuderia Success

        El test prueba la funcionalidad de agregar un Piloto a
        la escuderia. Los datos del piloto deben seguir el formato requerido.

        :param p1: Piloto que se agrega a la escuderia.
        :param e1: Escuderia para realizar el test
        :return:
        """
        p1 = Piloto("AAA", "Alni")
        e1 = Escuderia("Ferrari")

        self.assertEqual(e1.agregar_piloto(p1), True)

    def test_agregar_piloto_2(self):
        """
        Test Agregar Piloto a Escuderia Failure

        El test prueba que el piloto no exista en la Escuderia

        :param p1: Piloto que se agrega a la escuderia.
        :param p2: Piloto con id repetido para probar el test
        :param e1: Escuderia para realizar el test
        :return:
        """
        p1 = Piloto("AAA", "Alni")
        p2 = Piloto("AAA", "Pepe")
        e1 = Escuderia("Ferrari")

        e1.agregar_piloto(p1)
        self.assertEqual(e1.agregar_piloto(p2), False)

    def test_agregar_piloto_3(self):
        """
        Test Agregar Piloto a Escuderia Failure

        El test prueba que el objeto que se va a agregar a
        la escuderia, sea un piloto.

        :param m: Objeto tipo Mock que se agrega a la escuderia
        :param e1: Escuderia para realizar el test
        :return:
        """
        p1 = mock(Piloto)
        e1 = Escuderia("Ferrari")

        self.assertEqual(e1.agregar_piloto(p1), False)

    def test_eliminar_piloto_1(self):
        """
        Test Eliminar piloto existente no activo de Escuderia

        El test prueba que se elimine un piloto existente
        de la escuderia y que el piloto eliminado no sea un
        piloto activo

        :param p1: Piloto existente en la escuderia
        :param p2: Piloto existente en la escuderia
        :param p3: Piloto existente en la escuderia y que sera eliminado
        :return:
        """
        p1 = Piloto("AAA", "Piloto A")
        p2 = Piloto("BBB", "Piloto B")
        p3 = Piloto("CCC", "Piloto C")
        e1 = Escuderia("Ferrari")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e1.agregar_piloto(p3)

        self.assertEqual(e1.eliminar_piloto(p3), True)

    def test_eliminar_piloto_2(self):
        """
        Test Eliminar piloto no existente de Escuderia

        El test  prueba que no se puede eliminar un
        piloto que no existe en la escuderia, es decir
        comprueba los parametros de entrada antes de eliminar

        :param p1: Piloto existente en la escuderia
        :param p2: Piloto existente en la escuderia
        :param p3: Piloto existente en la escuderia y que sera eliminado
        :return:
        """
        p1 = Piloto("AAA", "Piloto A")
        p2 = Piloto("BBB", "Piloto B")
        p3 = Piloto("CCC", "Piloto C")
        e1 = Escuderia("Ferrari")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)

        self.assertEqual(e1.eliminar_piloto(p3), False)

    def test_eliminar_piloto_3(self):
        """
        Test Eliminar piloto existente activo de Escuderia

        El test prueba que se elimine un piloto existente
        de la escuderia y que el piloto eliminado no sea un
        piloto activo

        :param p1: Piloto Activo existente en la escuderia
        :param p2: Piloto Activo existente en la escuderia  y que sera eliminado
        :param p3: Piloto No Activo existente en la escuderia
        :return:
        """
        p1 = Piloto("AAA", "Piloto A")
        p2 = Piloto("BBB", "Piloto B")
        p3 = Piloto("CCC", "Piloto C")
        e1 = Escuderia("Ferrari")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e1.agregar_piloto(p3)

        e1.definir_pilotosActivos(p1, p2)

        self.assertEqual(e1.eliminar_piloto(p2), True)

    def test_definir_pilotos_activos_1(self):
        """
        Test definir Pilotos activos

        El test prueba que se dos pilotos sean activos en la
        escuderia.

        :param p1: Piloto no Activo Para hacer el test
        :param p2: Piloto no Activo Para hacer el test
        :param p3: Piloto no Activo Para hacer el test
        :param e1: Escuderia para el test
        :return:
        """
        p1 = Piloto("AAA", "Piloto A")
        p2 = Piloto("BBB", "Piloto B")
        p3 = Piloto("CCC", "Piloto C")
        e1 = Escuderia("Ferrari")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e1.agregar_piloto(p3)

        self.assertEqual(e1.definir_pilotosActivos(p1, p2), True)

    def test_definir_pilotos_activos_2(self):
        """
        Test definir Pilotos activos Faulire

        El test prueba que los dos objetos que se pasan
        sean Pilotos para que sean activos

        :param p1: Piloto no Activo Para hacer el test
        :param p2: Piloto no Activo Para hacer el test
        :param p3: Mock de tipo Piloto para hacer el test
        :param e1: Escuderia para el test
        :return:
        """
        p1 = Piloto("AAA", "Piloto A")
        p2 = Piloto("BBB", "Piloto B")
        p3 = mock(Piloto("CCC", "Piloto C"))
        e1 = Escuderia("Ferrari")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)
        e1.agregar_piloto(p3)

        self.assertEqual(e1.definir_pilotosActivos(p1, p3), False)

    def test_sustituir_piloto_1(self):
        """
        Test sustituir piloto de escuderia

        El test comprueba que la sustitucion de un piloto
        en la escuderia sea correcta

        :param p1: Piloto de la escuderia
        :param p2: Piloto de la escuderia
        :param p3: Piloto que va a sustituir a otro
        :return:
        """

        p1 = Piloto("AAA", "Piloto A")
        p2 = Piloto("BBB", "Piloto B")
        p3 = Piloto("CCC", "Piloto C")
        e1 = Escuderia("Ferrari")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)

        self.assertEqual(e1.definir_pilotosActivos(p1, p3), True)

    def test_sustituir_piloto_2(self):
        """
        Test sustituir piloto de escuderia failure

        El test comprueba que la sustitucion de un piloto
        en la escuderia reciba los objetos correctos

        :param p1: Piloto de la escuderia
        :param p2: Piloto de la escuderia
        :param p3: Mock de tipo piloto que va a intentar sustituir a otro piloto
        :return:
        """

        p1 = Piloto("AAA", "Piloto A")
        p2 = Piloto("BBB", "Piloto B")
        p3 = mock(Piloto("CCC", "Piloto C"))
        e1 = Escuderia("Ferrari")

        e1.agregar_piloto(p1)
        e1.agregar_piloto(p2)

        self.assertEqual(e1.definir_pilotosActivos(p1, p3), False)