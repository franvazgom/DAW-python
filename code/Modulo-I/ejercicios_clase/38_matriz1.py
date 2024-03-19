
def print_matrix(M):
    print(M)

def print_matrix_2(M):    
    for fila in M:
        print(fila)

def print_matrix_3(M):    
    filas = len(M)
    cols = len(M[0])
    for i in range(filas):
        for j in range(cols):
            print(M[i][j], end='\t')
        print()

def sum_matrix(A, B):
    filas = len(A)
    cols = len(A[0])
    for i in range(filas):
        for j in range(cols):
            print(A[i][j] + B[i][j], end='\t')
        print()

def main():
    #Matriz de 3 x 4
    A = [[4,3,5], [9,23,56], [0,-1,45]]
    B = [[2,3,1], [1,1,3], [0,7,2]]
    
    print_matrix(A)
    print_matrix_2(A)
    print('*'*50)
    print_matrix_3(A)
    print('*'*50)
    sum_matrix(A, B)


if __name__ == '__main__':
    main()