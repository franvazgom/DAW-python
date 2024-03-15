

# la función resta en el argumento n2, si no lo envían en la llamada, entonces se convierte en 5
def resta(p1=9, n2=5):
    res = p1 - n2
    return res

def pide_numero(): 
    return int(input("Dame un número: "))

def main():
    n1 = pide_numero()
    n2 = pide_numero()
    r_resta = resta(n1, n2)
    print(f'Resta = {r_resta}')

    r_resta = resta(30)
    print(f'Resta = {r_resta}')

    r_resta = resta()
    print(f'Resta = {r_resta}')



if __name__ == '__main__':
    main()
