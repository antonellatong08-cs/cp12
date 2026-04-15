
def printallfactors():
    number = int(input('Enter a number: '))
    count = 0
    for i in range(1 , number+1):
        if number % i == 0:
            count += 1
            print(count)
printallfactors()
# between number from 5000 to 10000 which of the number has the greatest number of factors

def numoffactors():
    count = 0
    for i in range(1 , number+1):
        if number % i == 0:
            count += 1
            print(count)
print(numoffactors(40))
print(numoffactors(41))

def isprime(n):
    cut=0
    for i in range(2,n):
        if n%i==0:
            cut+=1
            return 1


        else:
            cut+=1

            

