# Sublistas pares e impares
### Tema: Listas 

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Desarrolla un programa que, a partir de una lista de números enteros que recibirá del usuario, permita crear y desplegar dos sublistas, una sublista con valores pares y otra sublista con valores impares. 

## Entrada
Cero o más valores enteros, uno en cada renglón. Finaliza la captura con un *

## Salida
Se muestra una salida tal como se ilustra a continuación:
```
PARES
[2, 4, 8]
IMPARES
[1, 5]
```
La palabra PARES en mayúscula en un renglón y posteriormente el despliegue la lista de pares y de manera similar los impares, tal como se muestra en el ejemplo. Respeta el orden y no uses letreros para solicitar las entradas de datos.

## Ejemplos de ejecución del programa
### Entrada
```
>>> 2
>>> 4
>>> 1
>>> 8
>>> 5
>>> *
```
### Salida
```
PARES
[2, 4, 8]
IMPARES
[1, 5]
```
### Entrada
```
>>> *
```
### Salida
```
PARES
[]
IMPARES
[]
```