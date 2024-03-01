'''
Programa que utiliza la variable predefinida __name__
'''

def pide_numero():
    return int(input("Teclea un numero: "))

def main():
    print("La suma de los numeros es: ", pide_numero() + pide_numero())

if __name__ == '__main__':
    main()

