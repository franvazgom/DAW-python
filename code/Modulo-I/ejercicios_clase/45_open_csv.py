import os

def print_matrix(M):
    for line in M:
        for col in line:
            print(f'{col}'.rjust(12), end='')
        print() #Enter

def get_number(x):
    if '.' in x:
        return float(x)
    elif x.isnumeric():
        return int(x)
    else:
        return x

def convert_number(M):
    for i in range(len(M)):
        M[i]= list(map(get_number, M[i]))

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
    convert_number(matriz)
    print_matrix(matriz)


if __name__ == '__main__':
    main()
