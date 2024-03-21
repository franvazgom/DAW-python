import math
linea = "-"*50 + "\n"
print(linea + "-- Teoría de números \n" + linea)
print ("ceil(x) -> Regresa el entero más pequeño >= x; ", "ceil(3.1) = ", math.ceil(3.1))
print ("ceil(x) -> Regresa el entero más pequeño >= x; ", "ceil(-3.1) = ", math.ceil(-3.1))
print ("comb(n,k) -> Regresa las combinaciones sin repetición al seleccionar k elementos de n ", "comb(3,2) = ", math.comb(3,2))
print ("floor(x) -> Regresa el entero más grande <= x ", "floor(3.8) = ", math.floor(3.8))
print ("floor(x) -> Regresa el entero más grande <= x ", "floor(-3.8) = ", math.floor(-3.8))
print ("fabs(x) -> Regresa el valor absoluto de x; ", "fabs(-3.5) = ", math.fabs(-3.5))
print("factorial(x) -> Regresa el factorial de x; ", "factorial(5) = ", math.factorial(5))
print ("trunc(x) -> Regresa la parte entera de x ", "trunc(3.7) = ", math.trunc(3.7))
# fmod se prefiere para números con punto flotante (por la precisión matemática)
print ("fmod(x,y) -> Regresa el módulo de x con y ", "fmod(3.5,2.1) = ", math.fmod(3.5, 2.1))
# % se prefiere para números enteros
print ("x%y -> Regresa el módulo de x con y ", "3.5 % 2.1) = ", 3.5%2.1)

# ##################
print(linea + "-- potencias y logaritmos \n" + linea)
'''
exp
log
pow
sqrt
'''

# ##################
print(linea + "-- funciones trigonométricas \n" + linea)
'''
cos
sin
tan
'''

# ##################
print(linea + "-- Conversiones angulares \n" + linea)
'''
degrees
radians
'''

# ##################
print(linea + "-- Constantes \n" + linea)
'''
pi
e
inf
'''