

def main():
    cm = int(input("cm:"))
    km = cm // 100000
    residuo = cm % 100000
    m = residuo // 100
    cm = residuo % 100

    print(km, m, cm)
    
if __name__ == "__main__":
    main()