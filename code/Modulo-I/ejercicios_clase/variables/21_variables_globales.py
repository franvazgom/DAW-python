
#Variable GLOBAL 
x = 10
def spam():
    x = 5
    print(x)

def funcx():
    x = 10
    print(x)

def main():
    global x
    spam()
    print(x)
    x = 7
    print(x)

if __name__ == '__main__':
    main()