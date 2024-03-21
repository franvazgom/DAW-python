
def is_vowel(c):
    vowels = "AEIOU"
    value = c.upper() in vowels
    return value

def main():
    """ 
    Existen 3 formas de crear una lista 
    1.- Usando un ciclo
    2.- Usando Maps -> list
    3.- Re escribir un for-loop en una sola línea
    Sintaxis:  new_list = [ expression for member in iterable ]

    List comprehension return a list and the map return a map object
    """

    # numbers = []
    # for i in range(11):
    #     numbers.append(i)
    # print(numbers)

    numbers = [i for i in range(11) ]
    print(numbers)
    squares = [n ** 2 for n in numbers ]
    print(squares)

    nombres = ['Paula', 'Rosa', 'Fernando', 'Juan', 'Maricarmen', 'Liliana']

    f_nombres = [ f'archivo{s}.txt' for s in nombres ]
    print(f_nombres)
    
    # Filtrado, la forma más común para agregar una condición lógica es agregar la condición 
    # al final de la expresión
    
    cadena = "Hola esto es una prueba de caracteres raros no muy usados"
    vocales = [ v for v in cadena if v in "aeiou" ]
    print(vocales)

    vocales2 = [ v for v in cadena if is_vowel(v) ]
    print(vocales)
    
    is_v = lambda c:c.upper() in "AEIOU"
    vocales3 = [ v for v in cadena if is_v(v) ]
    print(vocales3)

if __name__ == '__main__':
    main()