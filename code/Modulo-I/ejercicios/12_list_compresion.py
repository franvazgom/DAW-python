""" 
Existen 3 formas de crear una lista 
1.- Usando un ciclo
2.- Usando Maps -> list
3.- Re escribir un for-loop en una sola línea
Sintaxis:  new_list = [ expression for member in iterable ]

List comprehension return a list and the map return a map object
"""
numbers = [1,2,3,4,5]
squares = [n ** 2 for n in numbers]
print(squares)


# Filtrado, la forma más común para agregar una condición lógica es agregar la condición 
# al final de la expresión
cad = "Hola, esto es un mensaje de pruebas."
vocales = [v for v in cad if v in "aeiou"]
print(vocales)

# Se puede mover a una función, por ejemplo.
def is_vowel(c):
    return c.upper() in 'AEIOU'
voc = [v for v in cad if is_vowel(v)]
print(voc)

# Se puede mover a una función lambda
f_vowel = lambda c:c.upper() in 'AEIOU'
voc = [v for v in cad if f_vowel(v)]
print(voc)

numbers = [-3, -2, -1, 0, 1, 2, 3]
nuevo = [n if n>0 else -n for n in numbers]
print(nuevo)