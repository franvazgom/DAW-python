import random
# Lista global
nombres = ['Francisco', 'Juan', 'Rosa', 'María', 'Fernanda', 'Moises', 'Julia', 'Húgo']  
apellidos = ['Fernández', 'Juárez', 'Martínez', 'Vázquez', 'Gómez', 'Salcedo']

def regresa_nombre_aleatorio():
    nombre = nombres[random.randint(0,len(nombres)-1)]
    ap_paterno = apellidos[random.randint(0,len(apellidos)-1)]
    ap_materno = apellidos[random.randint(0,len(apellidos)-1)]
    persona = nombre + " " + ap_paterno + " " + ap_materno
    return persona

def elimina_acentos(x):
    # acentos = ['á', 'é', 'í', 'ó', 'ú']
    # vocales = ['a', 'e', 'i', 'o', 'u']
    acentos = 'áéíóú'
    vocales = 'aeiou'
    for i in range(len(acentos)):
        x = x.replace(acentos[i], vocales[i])
    return x


def main():
    personas = []
    for _ in range(10):
        nombre = elimina_acentos(regresa_nombre_aleatorio())
        personas.append(nombre)
    
    for persona in personas:
        print(persona)
    
        

if __name__ == '__main__':
    main()