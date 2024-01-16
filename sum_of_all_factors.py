# sum of all factors of a number

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    if n % i == 0:
        sum += i
print("Sum of all factors of", n, "is", sum)
