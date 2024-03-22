
def main():
    f = open("archivo_pruebas.txt")
    content = f.read()
    print(content)
    print(type(content))
    f.close()


    f = open("archivo_pruebas.txt", "r", encoding='UTF-8')
    content = f.read()
    print(content)
    print(type(content))
    f.close()

    f = open("archivo_pruebas.txt", "r", encoding='UTF-8')
    lineas = f.readlines()
    print(lineas)
    print(type(lineas))
    f.close()


    f = open("archivo_pruebas.txt", "r", encoding='UTF-8')
    lineas = f.readlines()
    for linea in lineas:
        if '\n' in linea:
            linea = linea[:-1]
        print(linea)
    f.close()

    f = open("archivo_pruebas.txt", "r", encoding='UTF-8')
    for linea in f:
        if '\n' in linea:
            linea = linea[:-1]
        print(linea)
    f.close()

if __name__ == '__main__':
    main()