
def main():
    name = input('Teclea tu nombre: ')
    age = int(input("Edad: "))
    if name == 'Alice':
        print("Hola Alice")
        print("Bienvenida")    
    elif age < 12:
        print("Hola kiddo")
    else:
        print("Tu no eres Alice y tampoco tienes menos de 12.")
    
    print("Adios!!!!")


if __name__ == '__main__':
    main()
