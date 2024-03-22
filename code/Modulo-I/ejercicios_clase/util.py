import os

def print_matrix(M, head=False):
    if head:
        M = M[:15]
    for line in M:
        for col in line:
            print(f'{col}'.rjust(11), end='')
        print() #Enter


def write_file(file_name, data):    
    path = os.path.dirname(__file__) + '/data/'
    with open(path + file_name, 'w', encoding='UTF-8') as f:
        for row in data:            
            row = list(map(str, row))            
            line = ','.join(row) + '\n'
            f.write(line)

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

def read_file(file_name):
    tabla = []
    path = os.path.dirname(__file__) + '/data/'
    with open(path+file_name, 'r', encoding='UTF-8') as f:
        for line in f:
            renglon = line.split(",")
            tabla.append(renglon)
    return tabla

def clean_data(M):
    for linea in M:
        linea[-1] = linea[-1][:-1] if '\n' in linea[-1] else linea[-1]

def main():
    pass

if __name__ == '__main__':
    main()