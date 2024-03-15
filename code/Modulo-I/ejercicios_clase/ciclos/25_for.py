import random

def main(): 
    
    # name = input("Nombre: ")
    # n = int(input("Teclea N: "))
    # for i in range(n):
    #     print(f"{name} iteración: {i}")

    # for i in range(5,12):
    #     print(i)

    # i = 5
    # while i < 12:
    #     print(i)
    #     i = i + 1
        
    # for i in range(2, 10, 2):
    #     print(i)

    # for i in range(20, 5, -5):
    #     print(i)

    for i in range(10):
        print(f"{i}: {random.randint(1,100)}")


if __name__ == '__main__':
    main()