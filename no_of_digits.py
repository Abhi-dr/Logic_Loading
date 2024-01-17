def count_digits(number):
    num_digits = 0
    abs_number = abs(number)  # handeling negative numbers

    # Count digits using a loop
    while abs_number > 0:
        abs_number //= 10
        num_digits += 1

    return num_digits

# Example usage:
number_to_check = 12345
result = count_digits(number_to_check)

print(f"The number of digit s in {number_to_check} is: {result}")
