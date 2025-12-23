def number_pattern(n):
    error = validate_number(n)
    if error:
        return error

    return " ".join(str(value) for value in range(1, n+1))


def validate_number(num):
    if not isinstance(num, int):
        return "Argument must be an integer value."
    if num < 1:
        return "Argument must be an integer greater than 0."
    return None

print(number_pattern(4))
