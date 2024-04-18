# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    ( 
        ["003","marzo","021"], 
        ["Dame el día: ","Dame el mes: ","Dame el año: ", "La fecha es: 03/03/21"],
        "Revisa el formato de las entradas (número de caracteres, minúsculas, mayúsculas, etc.)"
    ),
    ( 
        ["3","Marzo","2021"], 
        ["Dame el día: ","Dame el mes: ","Dame el año: ", "La fecha es: 03/03/21"],
        "Revisa el formato de las entradas (número de caracteres, minúsculas, mayúsculas, etc.)"
    )
]