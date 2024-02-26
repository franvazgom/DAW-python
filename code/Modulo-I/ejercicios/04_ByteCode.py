import dis

def main():
    # Comentario de una línea
    print ("Esto es una suma")
    x = 4
    y = 23
    res = x + y
    print(res)

dis.dis(main)