n =input()
length = len(n)
for i in range(1, length):
    left = n[:i]
    right = n[i:]
    if left == left[ ::-1] and right == right[::-1]:
        print("yes")
        break
else:
        print("no")