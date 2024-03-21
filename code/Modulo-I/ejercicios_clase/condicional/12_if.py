
def main():
    name = input('Teclea tu nombre: ')
    age = int(input("Edad: "))
    if name == 'Alice':
        print("Hola Alice")
        print("Bienvenida")    
    elif age < 12:
        print("Hola kiddo")    
    elif age > 2000:
        print("Tu eres un vampir@")
        print("-->>> ")
    elif age > 100:
        print("Eres muy muy grande!!")
    else:
        print("////////////////////////////")
    print("Adios!!!!")


if __name__ == '__main__':
    main()
