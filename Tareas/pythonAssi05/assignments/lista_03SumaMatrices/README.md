# Suma Matrices
Matrices Suma MAtreices

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```

<h3>Suma de matrices</h3>
Desarrolla una función en Python que reciba dos matrices de números enteros y calcule su suma.
La suma de matrices toma dos matrices del mismo tamaño y regresa una matriz que contiene la suma los elementos que se encuentran en la misma posición:
Ejemplo:
 [ [ 2,   2], + [ [5,  8],  = [ [7, 10],
...[5,    4]].....[4, 10]]......[9, 14]]

En caso de que las matrices no sean del mismo tamaño se deberá mostrar el mensaje "Las matrices no son del mismo tamaño". 
Nota: Se debe incluir una función auxiliar que pida por teclado los valores de la matriz renglón por renglón, y genere la matriz correspondiente.

Entradas 
Números enteros separando los valores por espacios y que representan un renglón de la matriz.
Se sugiere utilizar la función <b>split</b> para generar una lista a partir de los datos dados en cada renglón. Para indicar el fin de la matriz ya no se teclea ningún número solo se presiona <b>enter</b>

Salida
La matriz resultante al sumar las dos matrices recibidas como entrada, o  el mensaje "Las matrices no son del mismo tamaño"

Ejemplos de ejecución del programa:
```
>>> 1 2
>>> 3 4
>>>  <------------------ enter sin teclear nada
>>> 5 6
>>> 6 1
>>>  <------------------ enter sin teclear nada
[ [6, 8], [9, 5] ]

>>> 1 2 1
>>>  <------------------ enter sin teclear nada
>>> 1 2
>>>  <------------------ enter sin teclear nada
```
Las matrices no son del mismo tamaño

NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.
