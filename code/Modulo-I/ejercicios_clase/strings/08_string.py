import math
str1 = f'El valor de pi es: {math.pi}'
print(str1)

print(f'El valor de Pi a 4 decimales es: {math.pi:.4f}')
print(f'El valor de Pi a 15 decimales es: {round(math.pi,15)}')
print(f'El valor de Pi redondeado: {round(math.pi)}')

nomb1 = 'Francisco'
ap1 = 'Vázquez'
edad1 = 48

nomb2 = 'Laura'
ap2 = 'Fernández'
edad2 = 32

nomb3 = 'Juan'
ap3 = 'Gómez'
edad3 = 9

print() #Enter
print(f'{"Nombre":15}{"Apellido":15}{"Edad":6}')
print(f'{nomb1:15}{ap1:15}{edad1:6}')
print(f'{nomb2:15}{ap2:15}{edad2:6}')
print(f'{nomb3:15}{ap3:15}{edad3:6}')







