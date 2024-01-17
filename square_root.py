def print_square_root(number):
    if number < 0:
        print("Square root is undefined for negative numbers.")
    else:
        square_root = number ** 0.5
        print(f"The square root of {number} is: {square_root}")

# Example usage:
number_to_sqrt = 25
print_square_root(number_to_sqrt)
