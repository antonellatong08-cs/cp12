n = int(input())
count = 0
while n != 1:
    if n % 2 == 1:
        n = n * 3 + 1
    else:
        n = n // 2
    count += 1
print(count)