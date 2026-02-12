p = int(input())
c = int(input())
score = 50 * p - 10 * c
if p > c:
    print (score + 500)
else:
    print (score)