def validate_int(number):
    """
    Validates if given input is a valid integer.

    Args:
        number (str): The value to be validated.

    Returns:
        int: The validated integer.

    Raises:
        ValueError: If the given input is not a valid integer.
    """
    try:
        return int(number)
    except ValueError as e:
        raise ValueError(f"Error: {number} is not a valid integer!", e) from e


def validate_float(number):
    """
    Validates if given input is a valid float.

    Args:
        number: The value to be validated.

    Returns:
        float: The validated float.

    Raises:
        ValueError: If the given input is not a valid float.
    """
    try:
        return float(number)
    except ValueError as e:
        raise ValueError(f"{number} is not a valid float!", e) from e


def validate_price(number):
    validate_int(number)
    validate_float(number)
