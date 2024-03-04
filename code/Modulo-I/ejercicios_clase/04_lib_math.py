'''
Programa para verificar el funcionamiento 
de la librería math
'''
import math  # import se utiliza para "importar" un librería

print("floor(3.9) => ", math.floor(3.9))
print("floor(3.1) => ", math.floor(3.1))
print("ceil(3.9) => ", math.ceil(3.9))
print("ceil(3.1) => ",  math.ceil(3.1))

print("Combinaciones de pares en 3 elementos: ", math.comb(3,2))
print("Permutaciones de pares en 3 elementos: ", math.perm(3,2))

print("Maximo comun divisor del 8,64 = ", math.gcd(8,64))
print("Maximo comun divisor del 6,9 = ", math.gcd(6,9))
print("Maximo comun divisor del 8,5 = ", math.gcd(8,5))

print("Pi = ", math.pi)
print("Coseno de 90 grados = coseno de pi / 2 = ", math.cos(math.pi / 2))
print("Coseno de 90 grados = coseno de pi / 2 = ", round(math.cos(math.pi / 2),2))
