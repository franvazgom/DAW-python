'''
map() Función que regresa un "iterador" del resultado después de aplicar una "función dada" 
a cada uno de los elementos "iterables" (lista, tupla, etc)
Sintaxis:
    map(fun, iter)
    fun: función que se ejecuta con cada elemento iterable
    iter: Objeto iterable (lista, tupla..)
'''

def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]

result = list(map(square, numbers))
print(result)



