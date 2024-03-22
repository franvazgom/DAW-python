
def operaciones(n1, n2):
    suma = n1 + n2
    resta = n1 - n2
    mult = n1 * n2
    return suma, resta, mult


def main():
    #Asignación multiple
    x, y, z = operaciones(10, 5)
    print(x, y, z)
    print("-"*50)
    # Ejemplo para recorrer una lista
    personas = ['Francisco', 'Juan', 'Rosa', 'María', 'Fernanda', 'Moises']    
    for persona in personas:
        print(persona)        
    print("-"*50)
    for i in range(len(personas)):
        print(f'indice: {i} -> {personas[i]}')    
    print("-"*50)
    
    for indice, elemento in enumerate(personas):
        print(indice, '->', elemento)
    


if __name__ == '__main__':
    main()