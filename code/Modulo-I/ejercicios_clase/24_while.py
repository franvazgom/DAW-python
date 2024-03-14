
def main(): 
    while True:
        # LOS NOMBRES VÁLIDOS son: Juan y Pedro
        nombre = input("Quien eres? ")
        if nombre != "Juan" and nombre != "Pedro":
            continue # Se pasa a la siguiente ITERACIÓN
        password = input("Password:")
        if password == "hola":
            break #Rompe el ciclo
        print("Intenta nuevamente..")
        

if __name__ == '__main__':
    main()