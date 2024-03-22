import random

def main():
    lista = ['carlos', 'Francisco', 'Norma', 'Claudia', 'Natallia', 'BETO', 'antonio']
    print(lista)
    lista.insert(1, 'Maria')
    print(lista)
    lista.sort()
    print("Lista ordenada")
    print(lista)
    l2 = [5,3,7,8,2,3,1,2,3,4,2,3,1]
    l2.sort()
    print(l2)
    l2.reverse()
    print(l2)

    print("------------------------------------------")
    # random.choice
    elemento = random.choice(lista)
    print(elemento)
    elemento = random.choice(lista)
    print(elemento)
    print("------------------------------------------")
    # random.shuffle
    random.shuffle(lista)
    print(lista)
    random.shuffle(lista)
    print(lista)

    
    

if __name__ == '__main__':
    main()
