
def square(n):
    return n ** 2

func_redu = lambda x:x**2

fun_par = lambda x:True if x%2 == 0 else False


def largo(s):
    return len(s)

def main():
    # if corto
    # edad = int(input("Teclea edad: "))
    # if edad < 5:
    #     is_baby = True
    # else:
    #     is_baby = False
    
    #if corto
    # is_baby = True if edad < 5 else False
    # print(is_baby )

    numbers = [3,4,1,2,7,5]
    # Problema: Reemplazar los valores de la lista por el cuadrado de cada número
    # for i in range(len(numbers)):
    #     numbers[i] = square(numbers[i])
    # print(numbers)

    '''
    map() Función que regresa un "iterador" del resultado después de aplicar una "función dada" 
    a cada uno de los elementos "iterables" (lista, tupla, etc)
    Sintaxis:
        map(fun, iter)
        fun: función que se ejecuta con cada elemento iterable
        iter: Objeto iterable (lista, tupla..)
    '''
    # resultado = list(map(square, numbers))
    # print(resultado)
    
    # x = ['Hola', 'Mexico', 'Mundo mundial']
    # r2 = list(map(len, x))
    # print(r2)
    print(numbers)
    r3 = list(map(func_redu, numbers))
    print(r3)
    r4 = list(map(fun_par, numbers))
    print(r4)

    print(list(map(lambda x:x**2, numbers)))

    format_numeric = lambda n:f"{n:e}" if isinstance(n,int) else f"{n:,.2f}"
    print(format_numeric(12345321))
    print(format_numeric(12345321.2134))
    print(format_numeric(12345321.2164))

if __name__ == '__main__':
    main()