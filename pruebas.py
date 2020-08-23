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

    # Pruebas para la suma de vectores.
    def test_sumav(self):
        self.assertEqual(calculadora_imaginarios.sumav([(8, 3), (-1, -4), (0, -9)], [(8, -3), (2, 5), (3, 0)]),[(16, 0), (1, 1), (3, -9)])
        self.assertEqual(calculadora_imaginarios.sumav([(3, 2), (3, 4), (5, 6)], [(2, 1), (5, 4), (6, 3)]),[(5, 3), (8, 8), (11, 9)])

    # Pruebas para el inverso aditivo de un vector.
    def test_inversoaditivo(self):
        self.assertEqual(calculadora_imaginarios.inversoaditivo([(9, 3), (-1, -5), (6, -4)]), [(-9, -3), (1, 5), (-6, 4)])
        self.assertEqual(calculadora_imaginarios.inversoaditivo([(-5, 2), (3, 0), (0, -1)]), [(5, -2), (-3, 0), (0, 1)])

   # Pruebas para la multiplicación escalar de un vector.
    def test_multescalarvector(self):
        self.assertEqual(calculadora_imaginarios.multescalarvector((3, 2), [(6, 3), (0, 0), (5, 1), (4, 0)]), [(12, 21), (0, 0), (13, 13), (12, 8)])
        self.assertEqual(calculadora_imaginarios.multescalarvector((-1, 1), [(-2, 5), (-1, -1), (2, -9)]), [(-3, -7), (2, 0), (7, 11)])

    # Pruebas para la multiplicación escalar de una matriz.
    def test_multescalarmatrices(self):
        self.assertEqual(calculadora_imaginarios.multescalarmatrices((3,2),[[(4,5),(1,1)],[(2,1),(1,1)]]),[[(2,23),(1,5)],[(4,7),(1,5)]])
        self.assertEqual(calculadora_imaginarios.multescalarmatrices((-2,3),[[(3,-2),(8,-4)],[(4,-10),(-2,-8)]]),[[(0,13),(-4,32)],[(22,32),(28,10)]])

    # Pruebas para la transpuesta de una matriz.
    def test_matriztranspuesta(self):
        self.assertEqual(calculadora_imaginarios.matriztranspuesta([[(4,9),(1,-3)],[(5,1),(6,8)]]),[[(4,9),(5,1)],[(1,-3),(6,8)]])
        self.assertEqual(calculadora_imaginarios.matriztranspuesta([[(5,9),(-7,-5),(-1,-4)],[(8,2),(-3,-7),(7,-8)]]),[[(5,9),(8,2)],[(-7,-5),(-3,-7)],[(-1,-4),(7,-8)]])

    # Pruebas para la matriz conjugada.
    def test_matrizconjugada(self):
        self.assertEqual(calculadora_imaginarios.matrizconjugada([[(-6, 1), (3, 8)], [(2, -6), (3, 0)]]), [[(-6, -1), (3, -8)], [(2, 6), (3, 0)]])
        self.assertEqual(calculadora_imaginarios.matrizconjugada([[(5, 4), (3, 2), (5, 0)], [(1, 1), (6, 3), (8, 9)]]),[[(5,-4),(3,-2),(5,0)],[(1,-1),(6,-3),(8,-9)]])

    # Pruebas para la adjunta o daga de una matriz.
    def test_adjmatriz(self):
        self.assertEqual(calculadora_imaginarios.adjmatriz([[(7,7),(3,8),(8,4)],[(5,0),(8,-6),(-10,-1)]]),[[(7,-7),(5,0)],[(3,-8),(8,6)],[(8,-4),(-10,1)]])
        self.assertEqual(calculadora_imaginarios.adjmatriz([[(5,4),(6,5)],[(8,7),(6,6)]]),[[(5,-4),(8,-7)],[(6,-5),(6,-6)]])

    # Pruebas para el producto de matrices.
    def test_multimatriz(self):
        self.assertEqual(calculadora_imaginarios.multimatriz([[(-6,2),(0,6),(7,2)],[(6,9),(7,7),(-6,-6)],[(5,8),(-6,8),(6,9)]],[[(9,-6),(-3,-4),(5,-2)],[(3,6),(-1,-5),(0,-5)],[(9,9),(8,-4),(-8,-4)]]),
                         [[(-33, 153), (120, 0), (-44, -22)], [(87, 0),(-26,-117),(107,70)],[(0,165),(147,26),(69,-36)]])

    # Pruebas para la acción de matriz sobre vector.
    def test_accionMatriz(self):
        self.assertEqual(calculadora_imaginarios.accionmatrizvector([[(-1,5),(1,-7),(-6,3)],[(-3,-9),(2,-5),(1,-10)],[(-6,5),(6,-5),(3,-2)]],[(1,-3),(4,3),(-3,1)]),[(54,-32),(0,17),(41,30)])

    # Prueba para el producto interno de vectores.
    def test_innervector(self):
        self.assertEqual(calculadora_imaginarios.innervector([[2,-1],[-8,-5],[-2,-6]],[[6,-3],[5,-1],[-6,-2]]),(-36,11))

    # Prueba para la norma de vectores.
    def test_norma(self):
        self.assertEqual(calculadora_imaginarios.norma([[4, 5], [3, 1], [0, -7]]), 10)

    #Prueba para la distancia entre vectores.
    def test_distancia(self):
         self.assertEqual(calculadora_imaginarios.distancia([(2,7),(4,-1),(2,-4)],[(7,8),(2,-8),(1,4)]),12)
         self.assertEqual(calculadora_imaginarios.distancia([(9,-7),(-1,-6)],[(7,-8),(5,-9)]),7.0710678118654755)

    # Pruebas para la matriz unitaria.
    def test_isUnitaria(self):
        self.assertEqual(calculadora_imaginarios.isUnitaria([[(0,1),(1,0),(0,0)],[(0,0),(0,1),(1,0)],[(1,0),(0,0),(0,1)]]),False)
        self.assertEqual(calculadora_imaginarios.isUnitaria([[(1,0),(-1,1)],[(1,1),(1,0)]]),False)

    # Prueba para la matriz hermitiana.
    def test_isHermitiana(self):
        self.assertEqual(calculadora_imaginarios.isHermitiana([[(3, 0), (2, -1), (0, -3)], [(2, 1), (0, 0), (1, -1)], [(0, 3), (1, 1), (0, 0)]]), True)
        self.assertEqual(calculadora_imaginarios.isHermitiana([[(1, 0), (3, -1)], [(3, 1), (0, 1)]]), False)

    # Prueba para el producto tensorial.
    def test_productotensor(self):
        self.assertEqual(calculadora_imaginarios.productotensor([[(3, 2), (3, 1)], [(0, 2), (1, 2)]], [[(1, 3), (0, 2)], [(1, 1), (1, 0)]]),
                         [[(-3, 11), (-4, 6), (0, 10), (-2, 6)], [(1, 5), (3, 2), (2, 4), (3, 1)],
                          [(-6, 2), (-4, 0), (-5, 5), (-4, 2)], [(-2, 2), (0, 2), (-1, 3), (1, 2)]])

if True:
    unittest.main()