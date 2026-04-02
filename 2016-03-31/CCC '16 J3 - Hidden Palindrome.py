s = input()
n = len(s)
for i in range(n):
    for j in range(i ,n):
        sub = s[i:j+1]
        if sub == sub[::-1]:
            lenth = max(len(sub),len(sub[::-1]))
print(lenth)