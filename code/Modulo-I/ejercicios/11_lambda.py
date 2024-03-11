'''
Funciones Lambda: Funciones sin nombre, se conoce como una función anónima
Sintaxis
    Puede tener varios argumentos, pero solo UNA expresión, la cual es evaluada y retornada
'''

def square(n):
    return n ** 2

A = [1,2,3,4,5]

res = list(map(square, A))
print(res)

res = list(map(lambda n:n**2, A))
print(res)

format_numeric = lambda n:f"{n:e}" if isinstance(n,int) else f"{n:,.2f}"

print(format_numeric(1434500))
print(format_numeric(3658734653.34343434))