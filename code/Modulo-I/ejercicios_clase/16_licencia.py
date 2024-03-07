
def main():
    edad = int(input("Edad: "))
    if edad > 0:
        if edad >= 18:
            credencial = input("Tienes credencial? s/n:  ")
            if credencial == 's' or credencial == 'n' :
                if credencial == 's':
                    print("Credencial otorgada")
                else:
                    print ('No cumples requisitos')
            else:
                print("Respuesta incorrecta")        
        else:
            print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")

if __name__ == "__main__":
    main()