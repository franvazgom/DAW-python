'''
Programa que utiliza la variable predefinida __name__
'''

def pide_numero():
    #Se pide un numero de teclado
    print("Teclea un numero: ")
    num = input()
    num = int(num)
    return num

def main():
    n1 = pide_numero()
    n2 = pide_numero()
    res = n1 + n2
    print("La suma de los numeros es: ", res)

if __name__ == '__main__':
    main()

