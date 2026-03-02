V = int(input())
votes = input()
Count_A = votes.count('A')
Count_B = votes.count('B')
if Count_A > Count_B:
    print("A")
elif Count_B > Count_A:
    print("B")
else:
    print("Tie")