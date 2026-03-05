import random
rock = 1
paper = 2
scissors = 3
computer = random.randint(1,3)
user = int(input("enter your choice: "))
while computer != user:
    if computer > user:
        print("computer wins")
        break
    elif computer < user:
        print("user wins")
        break
else:
    print("fair try again")