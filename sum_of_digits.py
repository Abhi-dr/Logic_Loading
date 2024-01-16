def sum_digits(number):
    sum_digits = 0
    abs_number = abs(number)  # Use abs to handle negative numbers

    # Sum digits using a loop
    while abs_number > 0:
        sum_digits += abs_number % 10
        abs_number //= 10

    return sum_digits

# Example usage:
number_to_check = 145
result = sum_digits(number_to_check)

print(f"The sum of digits in {number_to_check} is: {result}")
