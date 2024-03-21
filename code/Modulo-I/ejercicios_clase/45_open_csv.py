import os

def read_file():
    tabla = []
    path = os.path.dirname(__file__) + '/data/'
    with open(path+'datos.csv', 'r', encoding='UTF-8') as f:
        for line in f:
            renglon = line.split(",")
            tabla.append(renglon)
    return tabla

def clean_data(M):
    for linea in M:
        linea[-1] = linea[-1][:-1] if '\n' in linea[-1] else linea[-1]
    
def main():
    matriz = read_file()
    clean_data(matriz)
    print(matriz)


if __name__ == '__main__':
    main()
