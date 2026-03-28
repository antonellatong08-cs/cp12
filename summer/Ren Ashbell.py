n = int(input())
Ren = int(input())
strongest = True
for i in range(n-1):
    x = int(input())
    if x >= Ren:
        strongest = False
if strongest:
    print("YES")
else:
    print("NO")
