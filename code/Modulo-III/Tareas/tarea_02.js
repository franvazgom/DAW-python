/*
********************************************************************
* Ejercicio 01
********************************************************************
1.- Crear el archivo tarea_02.js
2.- Crear las siguientes funciones
-------------------------------------
-- 2.1- ObtenerPersona()
-------------------------------------
2.1- Crear un arreglo de apellidos y un arreglo de nombres, por ejemplo: 
    apellidos = ['Aguilar', 'Basurto', 'Fernández', 'Gómez', 'Juárez', 'Méndez', 'Malinalgo'];
    nombres = ['Ana', 'Armando', 'Carmen', 'Daniela', 'Ernesto', 'Francisco', 'Fernanda']; 
2.2- Crear un diccionario con un nombre, apellido paterno, apellido materno y edad que sea aleatorio, 
        tomando en cuenta los datos del arreglo. 
        La instrucción Math.random regresa un número aleatorio entre 0 y 1
        La instrucción Math.round redondea a un entero
        El método  .length  regresa el tamaño de un arreglo 
2.3.- Regresar el diccionario
-------------------------------------
-- 3. - agregaRenglon()
-------------------------------------
3.1.- Obtener una persona mediante la función ObtenerPersona
3.2.- Construir un "renglon html" con los datos obtenidos
3.3.- Agregar al final de la tabla "tablaPersonas" el renglon creado 
*/


/*
********************************************************************
* Ejercicio 02
********************************************************************
Filtrar los datos que aparecen en la tabla, mediante lo que se tenga en un campo de búsqueda
1.- En la parte superior de la tabla agregar un "input" tipo text, identificarlo como "inputTexto"
2.- Crear la función filtraInformacion
2.1.- Obtener el "valor" del input inputTexto 
2.2.- Para filtrar la información de acuerdo a lo que contenga inputTexto, es necesario "recorrer"
     cada uno de los renglones de tablaPersonas
     for(let i=0; i<$('#tablaPersonas tbody tr').length; i++) { ... }
     $('#tablaPersonas tbody tr').each(function(){ ... }); 
2.3.- Puede hacer uso de "indexOf" para verificar si un string en sub cadena de un tr
2.4.- Puede hacer uso de hide y show para filtrar la información  
3.- Sobrecargar la funcionalidad del evento "keyup", invocar a la función filtraInformacion
*/

/*
********************************************************************
* Ejercicio 03
********************************************************************
1.- Crear la función formatoTala()
2.- Agregar un estilo a los renglones impares, fondo (background #c1c1c1)
3.- Sobrecargar los eventos mouseover y mouseleave para cada renglon de tablaPersonas con el objetivo 
    de resaltar a fondo amarillo en el mouseover y regresarlo al original en el mouseleave
    Sobrecargar el evento dblclick para que se elimine un renglón de la tabla
*/
