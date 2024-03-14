import random
# Lista global
nombres = ['Francisco', 'Juan', 'Rosa', 'María', 'Fernanda', 'Moises', 'Julia']  
apellidos = ['Fernández', 'Juárez', 'Martínez', 'Vázquez', 'Gómez', 'Salcedo']

def regresa_nombre_aleatorio():
    nombre = nombres[random.randint(0,len(nombres)-1)]
    ap_paterno = apellidos[random.randint(0,len(apellidos)-1)]
    ap_materno = apellidos[random.randint(0,len(apellidos)-1)]
    persona = nombre + " " + ap_paterno + " " + ap_materno
    return persona

def main():
    personas = []
    for _ in range(10):
        personas.append(regresa_nombre_aleatorio())
    
    for persona in personas:
        print(persona)
    

if __name__ == '__main__':
    main()