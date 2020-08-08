# Gabriela Castro Santamaria
# Librería numeros imaginarios
# CNYT

import math

def suma (num1, num2):
    """Funcion que suma dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    ans = [0.0, 0.0]
    ans[0] = num1[0] + num2[0]
    ans[1] = num1[1] + num2[1]
    return ans

def resta (num1, num2):
    """Funcion que resta dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    ans = [0.0, 0.0]
    ans[0] = num1[0] - num2[0]
    ans[1] = num1[1] - num2[1]
    return ans

def mult (num1, num2):
    """Funcion que multiplica dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    ans = [0.0, 0.0]
    ans[0] = num1[0]*num2[0] - num1[1]*num2[1]
    ans[1] = num1[0] - num2[1] + num1[1] - num2[0]
    return ans

def modulo (num):
    """Funcion que regresa el modulo de un numero imaginario
    (list 1D) -> float"""
    ans = 0.0
    ans = (num[0] ** 2 + num[1] ** 2) ** (1/2)
    return ans

def polar(num):
    """Funcion que convierte un numero imaginario a su forma polar
    (list 1D) -> list 1D"""
    ans = [0.0, 0.0]
    ans[0] = modulo(num)
    ans [1] = math.radians(math.atan(num[1]/num[0]))
    return ans

def polarc (num):
    """Funcion que convierte un numero imaginario en su forma polar a su forma cartesiana
    (list 1D) -> list 1D"""
    ans = [0.0, 0.0]
    num[1] = math.degrees(num[1])
    ans[0] = num[0] * math.radians(math.cos(num[1]))
    ans[1] = num[0] * math.radians(math.sin(num[1]))
    return ans

def div (num1, num2):
    """Funcion que divide dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    num1 = polar(num1)
    num2 = polar(num2)
    ans = [0.0, 0.0]
    ans[0] = num1[0]/num2[0]
    ans[1] = num1[1] - num2[1]
    ans = polarc(ans)
    return ans

def conjugado (num):
    """Funcion que imprime el conjugado de un numero imaginario
    list 1D -> None"""
    print(num[0] , " ", "+", " ", num[1], "i")
