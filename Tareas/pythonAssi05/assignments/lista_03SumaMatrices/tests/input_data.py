# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["1 2","3 4","","5 6","4 1",""],
        ["","","","","","","[[6, 8], [7, 5]]"],
        "Error"
    ), 
    # Test case 2  
    (
        ["1 2 1","","1 2","5 8",""],
        ["","","","","","Las matrices no son del mismo tamaño"],
        "Error"
    )
]
