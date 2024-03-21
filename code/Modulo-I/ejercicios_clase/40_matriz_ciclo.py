
def recorre_por_columna(A):
    for j in range(len(A[0])):
        for i in range(len(A)):        
            print(A[i][j], end="\t")
        print() #Enter

def recorre_por_renglon(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end="\t")
        print() #Enter

def main():
    M = [[4,3,6], [9,8,7], [5,6,0], [3,3,3]]
    # recorre_por_renglon(M)
    recorre_por_columna(M)

if __name__ == '__main__':
    main()