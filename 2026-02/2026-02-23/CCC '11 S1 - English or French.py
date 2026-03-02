n = int(input())
t_count = 0
s_count = 0
for i in range(n):
    line = input()
    s_count += line.count('s') + line.count('S')
    t_count += line.count('t') + line.count('T')
if s_count > t_count:
    print("French")
elif s_count < t_count:
    print("English")
else:
    print("French")