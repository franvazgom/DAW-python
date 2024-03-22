# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["3","4"],
        ["","","La matriz no es cuadrada"],
        "La matriz no es cuadrada"
    ),   
    (
        ["3","3","1","2","3","4","5","6","7","8","9"],
        ["","","","","","","","","","","","[1, 5, 9]"],
        "Error"
    )  
     
]
