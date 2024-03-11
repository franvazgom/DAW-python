import random
# Función que recibe un número y lo almacena en la variable numero
# Regresa un string
def main():
    fortuna = obten_suerte()
    print(fortuna)

def obten_suerte():
    numero = random.randint(1,8)
    if numero == 1:
        return 'Hoy será un día caluroso'
    elif numero == 2:
        return 'Tendrás una visita inesperada..'
    elif numero == 3:
        return 'Juega con el número 3, es tu suerte'
    elif numero == 4:
        return 'Recibirás una mala noticia'
    elif numero == 5:
        return 'No salgas, te puedes lastimar'
    elif numero == 6:
        return 'Vas a recibir un punto extra'
    else:
        return 'Sin suerte..'

if __name__ == '__main__':
    main()
