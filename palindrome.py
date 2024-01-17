def is_palindrome(number):
    original_number = abs(number)  # Use abs to handle negative numbers
    reversed_number = 0
    temp_number = original_number

    # Reverse the digits
    while temp_number > 0:
        reversed_number = reversed_number * 10 + temp_number % 10
        temp_number //= 10

    # Check if the original number is equal to its reverse
    return original_number == reversed_number

# Example usage:
number_to_check = 121
result = is_palindrome(number_to_check)

if result:
    print(f"{number_to_check} is a palindrome.")
else:
    print(f"{number_to_check} is not a palindrome.")
z