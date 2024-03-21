

def main():
    numero = int(input("Numero: "))
    if numero < 0:
        print("NEGATIVO")    
        if numero == -5:
            print("El numero es el -5")
        else:
            print("No es el menos 5")
    elif numero == 0:
        print("CERO")
    else:
        print("POSITIVO")
    
    

if __name__ == "__main__":
    main()