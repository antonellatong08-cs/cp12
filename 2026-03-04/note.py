# pick a random target between 1 and 100
# repeat
    # ask the user for input
    # compare the input with the target number
    # print go higher or lower base on the comparison
# the user found the number
import random
target = random.randint(1,100)
running = True
while running == True:
    user = int(input("Enter a number: "))
    if user > target:
        print("lower")
    elif user < target:
        print("higher")
    else:
        print("correct")
        running = False
#count how many choices the user made to get it right
#ask what level the user what to play (easy 1-10 medium 1-100 hard 1-1000