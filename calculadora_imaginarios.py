# Gabriela Castro Santamaria
# Librería numeros imaginarios
# CNYT

import math

def suma (num1, num2):
    """Funcion que suma dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    ans1 = num1[0] + num2[0]
    ans2 = num1[1] + num2[1]
    return (ans1, ans2)

def resta (num1, num2):
    """Funcion que resta dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    ans1 = num1[0] - num2[0]
    ans2 = num1[1] - num2[1]
    return (ans1, ans2)

def mult (num1, num2):
    """Funcion que multiplica dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    ans1 = num1[0]*num2[0] - num1[1]*num2[1]
    ans2 = num1[0] - num2[1] + num1[1] - num2[0]
    return (ans1, ans2)

def div (num1, num2):
    """Funcion que divide dos numeros imaginarios, los numeros deben ser parejas ordenadas
    (list 1D, list 1D) -> list 1D"""
    num1 = polar(num1)
    num2 = polar(num2)
    ans = [0.0, 0.0]
    ans[0] = num1[0]/num2[0]
    ans[1] = num1[1] - num2[1]
    ans = polarc(ans)
    return (ans[0], ans[1])

def modulo (num):
    """Funcion que regresa el modulo de un numero imaginario
    (list 1D) -> float"""
    ans = (num[0] ** 2 + num[1] ** 2) ** (1/2)
    return ans

def polar(num):
    """Funcion que convierte un numero imaginario a su forma polar
    (list 1D) -> list 1D"""
    ans1 = modulo(num)
    ans2 = math.atan(num[1]/num[0])
    return (ans1, ans2)

def polarc (num):
    """Funcion que convierte un numero imaginario en su forma polar a su forma cartesiana
    (list 1D) -> list 1D"""
    ans1 = num[0] * math.cos(num[1])
    ans2 = num[0] * math.sin(num[1])
    return (ans1, ans2)

def conjugado (num):
    """Funcion que retorna el conjugado de un numero imaginario
    (list 1D) -> list 1D"""
    num[1] = num[1]*-1
    return (num[0], num[1])

