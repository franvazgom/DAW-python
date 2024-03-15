def main():
    # for i in range(50):
    #     if i % 3 == 0:
    #         continue
    #     print(f"i = {i}")
    #     if i > 10:
    #         break

    n = int(input("Cuantos multiplos de 2 o multiplo de 3 quieres imprimir: "))    
    li = int(input("En qué numero quieres iniciar? "))

    contador = 0
    numero = li
    while True:
        if numero % 2 == 0 or numero % 3 == 0:
            print(numero)
            contador = contador + 1
            if contador == n:
                break
        numero = numero + 1

if __name__ == '__main__':
    main()