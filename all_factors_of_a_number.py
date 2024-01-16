# create a python code to print all factors of a number n
# example: n=6, factors are 1,2,3,6

n = int(input("Enter a number: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")