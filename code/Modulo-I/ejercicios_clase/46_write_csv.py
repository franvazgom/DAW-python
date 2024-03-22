import random
import os

def print_matrix(M, head=False):
    if head:
        M = M[:15]
    for line in M:
        for col in line:
            print(f'{col}'.rjust(11), end='')
        print() #Enter

def generate_data():
    '''
        Año        Mes   Producto     Precio         S1         S2         S3         S4
       2020      Enero    Manzana       23.2         93         31        196         88
       2020      Enero       Pera       45.0        134        146        165        180
       2020      Enero    Naranja      33.15        100          5        115         11
       2020      Enero    Platano       12.0         91        130         56        165
        ...        
    '''
    anios = [i for i in range(2020, 2023)]
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']    
    productos = ['Manzana', 'Pera', 'Naranja', 'Platano', 'Uva', 'Papaya', 'Piña', 'Fresa', 'Mandarina']
    precios = [23.2, 45.0, 33.15, 12.0, 99.5, 42.0, 27.3, 105.1, 11.0]
    table = [['Año', 'Mes', 'Producto', 'Precio', 'S1', 'S2', 'S3', 'S4']]

    for anio in anios:
        for mes in meses:
            for i in range(len(productos)):
                record = [anio, mes, productos[i], precios[i], random.randint(0,200), \
                          random.randint(0,200), random.randint(0,200), random.randint(0,200)]
                table.append(record)
    return table

def convert_to_str(x):
    return str(x)

def write_file(file_name, data):
    '''
    Año,Mes,Producto,Precio,S1,S2,S3,S4
    2020,Enero,Manzana,23.2,93,31,196,88
    ....
    '''
    path = os.path.dirname(__file__) + '/data/'
    with open(path + file_name, 'w', encoding='UTF-8') as f:
        for row in data:
            #row = list(map(lambda x:str(x), row))
            #row = list(map(str, row))
            row = list(map(convert_to_str, row))
            line = ','.join(row) + '\n'
            f.write(line)


def main():
    data = generate_data()
    print_matrix(data, True)
    write_file('data_test.csv', data)

if __name__ == '__main__':
    main()