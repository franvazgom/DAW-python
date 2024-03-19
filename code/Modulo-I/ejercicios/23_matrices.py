
def imprime(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]}'.rjust(4),end='')
        print()


def imprime2(A):
    for renglon in A:
        print(renglon)

A=[[1,22,3],[434,5,26],[721,89,912]]

imprime(A)
