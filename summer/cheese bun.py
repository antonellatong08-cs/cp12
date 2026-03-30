W = int(input())
C = int(input())
if W == 3 and C >= 95:
    satisfaction = "absolutely"
elif W == 1 and C <= 50:
    satisfaction = "fairly"
else:
    satisfaction = "very"
print(f"C.C. is {satisfaction} satisfied with her pizza.")