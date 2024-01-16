def is_sum_of_factors_equal_to_factorial(number):
    # Calculate the sum of factors
    factors_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            factors_sum += i

    # Calculate the factorial
    factorial_value = 1
    for i in range(1, number + 1):
        factorial_value *= i

    # Check if the sum of factors is equal to the factorial
    return factors_sum == factorial_value

# Example usage:
number_to_check = int(input("Enter the number: "))
result = is_sum_of_factors_equal_to_factorial(number_to_check)

if result:
    print(f"The sum of factors of {number_to_check} is equal to its factorial.")
else:
    print(f"The sum of factors of {number_to_check} is not equal to its factorial.")
    