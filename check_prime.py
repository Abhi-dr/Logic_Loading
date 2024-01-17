def is_prime(number):
    if number <= 1:
        return False

    flag = True # Flag to indicate if number is prime or not

    for i in range(2, number):
        if number % i == 0:
            flag = False
            break

    return flag  # Return True if flag is False, meaning the number is prime

print(is_prime(6))
