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
    for _ in range(500):
        personas.append(regresa_nombre_aleatorio())
    
    #for persona in personas:
    #    print(persona)
    
    nombre = 'Francisco Vázquez Gómez' 
    if nombre not in personas:
        print(f"La persona> {nombre} no está")
    else:
        print(f"La persona {nombre} si se encuentra en la lista")
        print(f'Se encuentra en la posición: {personas.index(nombre)}')
        

if __name__ == '__main__':
    main()