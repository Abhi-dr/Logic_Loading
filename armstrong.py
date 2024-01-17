def count_digits(number):
    num_digits = 0
    abs_number = abs(number)  # handeling negative numbers

    # Count digits using a loop
    while abs_number > 0:
        abs_number //= 10
        num_digits += 1

    return num_digits


def is_armstrong(number):
    # Get the number of digits
    num_digits = count_digits(number)

    # Calculate the sum of the nth power of each digit
    sum = 0
    abs_number = abs(number)  # handeling negative numbers
    while abs_number > 0:
        digit = abs_number % 10
        sum += digit ** num_digits
        abs_number //= 10
        
    # Return True or False
    return sum == abs(number)
 
 
# Get user input
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(number):
    print(number, "is an Armstrong number")
    
else:
    print(number, "is not an Armstrong number")
    