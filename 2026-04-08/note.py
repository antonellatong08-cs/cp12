
def printallfactors():
    number = int(input('Enter a number: '))
    count = 0
    for i in range(1 , number+1):
        if number % i == 0:
            count += 1
            print(count)
printallfactors()
# between number from 5000 to 10000 which of the number has the greatest number of factors
