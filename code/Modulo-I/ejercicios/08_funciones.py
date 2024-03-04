def suma_enteros(n1 = None, n2 = 0):    
    if n1 == None or n2 == None:
        # Observa que si se ejecuta este return, la función termina
        return 0
    return n1 + n2

print(suma_enteros())
print(suma_enteros(8)) 
print(suma_enteros(10, 20)) 

#Llamada indicando de manera explicita los valores
print(suma_enteros(n2=10, n1=20))
print(suma_enteros(n1=20))
print(suma_enteros(10, n2=None))
