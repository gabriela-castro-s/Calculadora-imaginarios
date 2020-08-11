import unittest
import calculadora_imaginarios
import math

class unit_complejos(unittest.TestCase):

    #Pruebas para la suma.
    def test_suma(self):
        self.assertEqual(calculadora_imaginarios.suma((4, 5), (5, 2)), (9, 7))
        self.assertEqual(calculadora_imaginarios.suma((1, 5), (0, 2)), (1, 7))

    #Pruebas para la resta.
    def test_resta(self):
        self.assertEqual(calculadora_imaginarios.resta((1, 5), (0, 2)), (1, 3))
        self.assertEqual(calculadora_imaginarios.resta((3, 1), (4, 1)), (-1, 0))

    #Pruebas para la multiplicación.
    def test_mult(self):
        self.assertEqual(calculadora_imaginarios.mult((-2, -1), (-1, -2)), (0, 5))
        self.assertEqual(calculadora_imaginarios.mult((-2, -1), (1, -3)), (-5, 5))

    #Pruebas para la división.
    def test_div(self):
        self.assertEqual(calculadora_imaginarios.div((4, 12), (6, 2)), (1.2, 1.6))
        self.assertEqual(calculadora_imaginarios.div((0, 3), (-1, -1)), (-1.5, -1.5))

    #Pruebas para el módulo.
    def test_modulo(self):
        self.assertEqual(calculadora_imaginarios.modulo((4, -3)), (5))
        self.assertEqual(calculadora_imaginarios.modulo((6, -3)), (6.708203932499369))

    #Pruebas para la conversión de representación cartesiana a polar.
    def test_polar(self):
        self.assertEqual(calculadora_imaginarios.polar((-3, -1)), (3.1622776601683795, -2.819842099193151))
        self.assertEqual(calculadora_imaginarios.polar((1, 1)), (1.4142135623730951, 0.7853981633974483))

    #Pruebas para la conversión de representación polar a cartesiana.
    def test_polarc(self):
        self.assertEqual(calculadora_imaginarios.polarc((3, math.pi/3)), (1.5000000000000004, 2.598076211353316))
        self.assertEqual(calculadora_imaginarios.polarc((4, math.pi/6)), (3.464101615137755, 1.9999999999999998))

    #Pruebas para el conjugado.
    def test_conjugado(self):
        self.assertEqual(calculadora_imaginarios.conjugado([-2, -1]), (-2, 1))
        self.assertEqual(calculadora_imaginarios.conjugado([-2, 1]), (-2, -1))

if True:
    unittest.main()
