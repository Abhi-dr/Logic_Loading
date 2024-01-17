def reverse_number(number):
    reverse_number = 0

    # Reverse the number using a loop
    while number != 0:
        reverse_number = reverse_number * 10 + number % 10
        number //= 10

    return reverse_number

# Example usage:
number_to_reverse = 87904   
result = reverse_number(number_to_reverse)

print(f"The reverse of {number_to_reverse} is: {result}")
