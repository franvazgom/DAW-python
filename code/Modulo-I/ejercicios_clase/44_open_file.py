import os

def main():
    lineas = []
    # path = "C:/Users/Francisco/Documents/Developer/ProyectosGit/DAW-python/code/Modulo-I/ejercicios_clase/"
    path = os.path.dirname(__file__) + '/data/'
    with open(path+'archivo_pruebas.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            lineas.append(line)
    print(lineas)

if __name__ == '__main__':
    main()
