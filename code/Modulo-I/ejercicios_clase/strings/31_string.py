def main():
    # ejemplo 1
    x = 'Python es lo mejor'
    print(x.replace('o', 'x'))
    print(x)

    #ejemplo 2
    x = 'Python es lo mejor'
    x = x.replace('o', 'x')
    print(x)

    print('-'*50)
    x = "Hola Mundo, pruebas de LETRAS"
    print(x.lower())
    x = x.upper()
    # print(x.upper())
    print(x)
    print(x.isupper())
    print(x.islower())
    print(x)

    print('-'*50)
    print('cisco' in 'Francisco Vázquez')
    x = "Hola México"
    print('-'*50)
    print(x.startswith("Ho"))
    print(x.endswith("undo"))

    print('-'*50)
    x = "Hola"
    y = "main"
    print(x.rjust(50))
    print(y.rjust(50))
    print('-'*50)
    print(x.ljust(50,'*'))
    print(y.ljust(50,'*'))
    print('-'*50)
    print(x.center(50,'*'))
    print(y.center(50,'-'))

if __name__ == '__main__':
    main()