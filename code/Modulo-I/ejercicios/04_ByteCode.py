import dis

def main():
    print ("Esto es una suma")
    x = 4
    y = 23
    res = x + y
    print(res)

dis.dis(main)