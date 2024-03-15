
def main(): 
    contador = int(input("Cuanto vale contador: "))   
    while contador < 5:
        print(f"Hola, contador = {contador} ")
        contador = contador + 1
    print("Se terminó el ciclo")

    nombre = ""
    while nombre != 'tu nombre':
        print("Escribe tu nombre")
        nombre = input()

if __name__ == '__main__':
    main()