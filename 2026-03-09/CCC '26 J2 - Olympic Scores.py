a = []
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
D = int(input())
all = sum (a) - max(a) - min(a)
total = all * D
print(total)