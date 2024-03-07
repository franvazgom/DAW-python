

def main():
    #Se piden los 3 lados del triangulo
    x = int(input("lado 1: "))
    y = int(input("lado 2: "))
    z = int(input("lado 3: "))
    
    #Se valida que sea un triángulo
    if x < 0 or y < 0 or z < 0: 
        print("NO ES UN TRIANGULO")
    else: 
        if x + y > z and x + z > y and y + z > x: 
            if x == y and y == z:
                print("EQUILATERO")
            elif x == y or x == z or y == z:
                print("ISOSCELES")
            else:
                print("ESCALENO")
        else:
            print("NO ES UN TRIANGULO")
    
        

if __name__ == "__main__":
    main()