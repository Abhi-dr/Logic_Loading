# function to print even numbers from 1 to n

def even_from_1_to_n(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)
            
# Get user input
n = int(input("Enter a number: "))
even_from_1_to_n(n)  # Calling the function


