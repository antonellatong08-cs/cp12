a = input() + input() + input() + input() + input() + input()
Count_W = a.count('W')
if 5 <= Count_W <= 6:
    print("1")
elif 3 <= Count_W <= 4:
    print("2")
elif 1 <= Count_W <= 2:
    print("3")
else:
    print("-1")