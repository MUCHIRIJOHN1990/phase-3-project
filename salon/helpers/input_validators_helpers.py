def validate_int(number):
    """
    Validates if given input can be converted to an integer.

    Args:
        number: Value to be validated

    Raises:
        ValueError: If given input is not a valid integer
    """

    try:
        int(number)
    except:
        raise ValueError(f"Error: {number} is not a valid input!")


def validate_float(number):
    """
    Validates if given input is a float.

    Args:
        number: The input to be validated

    Raises:
        ValueError: If given input is not a float
    """

    if not isinstance(number, float):
        raise ValueError(f"Error: {number} is not a valid input!")
