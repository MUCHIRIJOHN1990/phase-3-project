def validate_int(number):
    try:
        int(number)
    except:
        raise ValueError(f"Error: {number} is not a valid input!")


def validate_string():
    pass


def validate_float():
    pass
