import pytest
import src.exercise
from tests.input_data import input_values

# Define the parametrization based on the inputs from the input_data file
@pytest.mark.parametrize('value, result, message', input_values)

def test_exercise(value, result, message):
    """
    Tests the code in src.exercise using the inputs from tests.input_data.
    Asserts that what is printed in the terminal is the same as
    the expected result.

    Parameters:
        value: list(str)
            The values that are used as input for the test.
            Usually strings, since we are simulating input from user.
        result: list(str)
            The expected output in the terminal, usually what the user prints
        message: str
            A hint string in case of an error
    """
    output = []

    def mock_input(input_s=None):
        """
        Create a mock input, where each input is obtained from
        the list of inputs. Appends the input to a list.

        Parameters:
            input_s: str
                Input from the test exercise.
        """
        if input_s is not None:
            output.append(input_s)
        else:
            output.append("")

        return value.pop(0)

    src.exercise.input = mock_input
    #src.exercise.print = lambda s : output.append(s)
    src.exercise.print = lambda *args: output.append(" ".join(map(str, args)))

    src.exercise.main()

    assert output == result, message
