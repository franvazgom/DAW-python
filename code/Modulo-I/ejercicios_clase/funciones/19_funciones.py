
def suma(n1, n2):
    res = n1 + n2
    return res

def resta(p1, n2):
    res = p1 - n2
    return res

def pide_numero(): 
    return int(input("Dame un número: "))

def main():
    n1 = pide_numero()
    n2 = pide_numero()
    r_suma = suma(n1, n2)
    r_resta = resta(n1, n2)
    print(f'La suma es: {r_suma}, resta = {r_resta}')

    r3 = resta(10, 4)    
    print(r3)
    r3 = resta(p1=10, n2=4)   # p1 se refiere al nombre del ARGUMENTO de la función. 
    print(r3)
    r3 = resta(n2=4, p1=10) 
    print(r3)
    # p1 = n1; significa que el argumento de la función con nombre p1 recibe el valor n1 definido en el main
    r3 = resta(p1=n1, n2=n2)   
    print(r3)

if __name__ == '__main__':
    main()
