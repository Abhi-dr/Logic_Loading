def print_last_digit(number):
    last_digit = abs(number) % 10  # Use abs to handle negative numbers
    print(last_digit)


n = 12345
print_last_digit(n)
