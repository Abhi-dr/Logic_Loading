import math

def check_and_print(number):
    if number % 2 == 1:  # Odd number
        print(f"{number} is an odd number. Factorial: {math.factorial(number)}")
    else:  # Even number
        sum_of_numbers = sum(range(1, number + 1))
        print(f"{number} is an even number. Sum of first {number} numbers: {sum_of_numbers}")

# Example usage:
number_to_check = 5
check_and_print(number_to_check)
