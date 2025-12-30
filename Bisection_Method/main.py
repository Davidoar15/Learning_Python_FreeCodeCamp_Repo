def square_root_bisection(number, tolerance=0.01, max_iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    low = 0
    high = max(1, number)
    iterations = 0

    while iterations < max_iterations:
        mid = (low + high) / 2
        squared = mid**2

        if squared > number:
            high = mid
        else:
            low = mid

        iterations += 1

    root = (low + high) / 2
    if abs(root**2 - number) <= tolerance:
        print(f"The square root of {number} is approximately {root}")
        return root

    print(f"Failed to converge within {max_iterations} iterations")
    return None
