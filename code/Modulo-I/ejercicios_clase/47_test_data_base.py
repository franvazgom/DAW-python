import util

# Solo suma enteros a partir de la columna 4
def sum_row(M, index_row):
    total = 0 
    record = M[index_row]
    record = record[4:]
    for value in record:
        total += value
    return total

# Se suma toda la columna (sin el encabezado)
def sum_column(M, index_col):
    total = 0
    # for line in M[1:]:
    for i in range(1, len(M)):
        total += M[i][index_col]
    return total

def add_total(M):
    M[0].append("Total")
    for i in range(1, len(M)):
        M[i].append(sum(M[i][4:]))


def init():
    data = util.read_file('data_test.csv')    
    util.clean_data(data)
    util.convert_number(data)    
    return data

def main():
    data = init()
    util.print_matrix(data, True)
    # x = sum_row(data,1)
    x = sum(data[1][4:])
    print(x)
    x = sum_column(data, 5)
    print(x)
    add_total(data)
    util.print_matrix(data, True)

if __name__ == '__main__':
    main()