# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    ["0", "1", "2", "3", "4", "*"],
    ["", "", "", "", "", "", "PARES", "[0, 2, 4]", "IMPARES", "[1, 3]"],
    ["La salida no cumple con el caso de prueba\nDebe haber 3 elementos en la lista de PARES y 2 en la lista IMPARES."]
    ),
    # Test case 2
    (
    ["*"],
    ["", "PARES", "[]", "IMPARES", "[]"],
    ["La salida no cumple con el caso de prueba\nAmbas sublistas deben estar vacias."]
    ),
    # Test case 2
    (
    ["0", "2", "4", "*"],
    ["", "", "", "", "PARES", "[0, 2, 4]", "IMPARES", "[]"],
    ["La salida no cumple con el caso de prueba\nSólo la sublista PARES tiene elementos."]
    )
    ]
