
def spam():
    x = 5
    return x

def funcx():
    x = 7
    x = spam()    
    return x

def main():
    x = 8
    x = funcx()
    print(x)

if __name__ == '__main__':
    main()