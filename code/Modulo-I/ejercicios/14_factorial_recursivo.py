import timeit

def factorial(n):
    espacios = '  '*(10 - n)
    if n == 0 or n == 1:        
        return 1
    else:        
        print(espacios + f' return {n} * factorial({n-1})')
        f = factorial(n - 1)
        print(espacios + f'  El factorial({n-1}) = {f}')
        return n * f

def fact_recursivo(n):
    if n == 0 or n == 1:        
        return 1
    else:        
        return n * fact_recursivo(n - 1)

def factorial_iterativo(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact


def main():
    n = int(input("n: "))
    # fact = factorial(n)
    # print(f'El factorial de {n} es: {fact}')

    fr = fact_recursivo(n)
    fi = factorial_iterativo(n)
    print(fr, fi)


    parametro = 900
    f1 = lambda:fact_recursivo(parametro)
    f2 = lambda:factorial_iterativo(parametro)

    t1 =  timeit.timeit(f1, number=1)
    t2 =  timeit.timeit(f2, number=1)

    print(t1, t2)

if __name__ == '__main__':
    main()