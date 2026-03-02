D = int(input())
E = int(input())
current = D
count = 0
while E > 0:
    op = input()
    Q = int(input())
    if op == "+":
        current += Q
    else:
        current -= Q
    E -= 1
print(current)