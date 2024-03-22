# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
  # Test case 1
  (
  ["*", "*"],
  ["", "", "L1=", "[]",  "L2=", "[]", "LORDENADA=", "[]"],
  ["La salida no cumple con el caso de prueba\nChecar el caso cuando L1 y L2 están vacías."]
  ),
  # Test case 2
  (
  ["2", "*", "1", "*"],
  ["", "", "", "", "L1=", "[2]", "L2=", "[1]", "LORDENADA=", "[1, 2]"],
  ["La salida no cumple con el caso de prueba\nChecar el caso para un valor en cada lista."]
  )
  ]
