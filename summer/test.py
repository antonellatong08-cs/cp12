A = int(input())
N = int(input())
x = 80 * (N + 1) - A * N
if x > 100:
    print(-1)
elif x < 0:
    print(0)
else:
    print(x)