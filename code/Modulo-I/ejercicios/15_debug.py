def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    r = factorial(5)
    print(f'El factorial de 5 es {r}')


if __name__ == '__main__':
    main()