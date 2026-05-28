def sumofdigit(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumofdigit(n // 10)

def numberofdigit(n):
    if n == 0:
        return 0
    else:
        return 1 + numberofdigit(n//10)

n = int(input("Enter a number: "))
print(numberofdigit(n))
print(sumofdigit(n))