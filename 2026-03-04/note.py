# pick a random target between 1 and 100
# repeat
    # ask the user for input
    # compare the input with the target number
    # print go higher or lower base on the comparison
# the user found the number
import random
import sys
print ("1. easy (1-10)")
print ("2. medium (1-100)")
print ("3. hard  (1-1000)")
choice= int(input())
if choice == "1":
    target = random.randint(1, 10)
elif choice == "2":
    target = random.randint(1, 100)
else :
    target = random.randint(1, 1000)
turns = 0
running = True
while running == True:
    user = int(input("Enter a number: "))
    turns += 1
    if user > target:
            print("lower")
    elif user < target:
            print("higher")
    else:
            print("correct")
            running = False
            print("it took you", turns, "turns")
#count how many choices the user made to get it right
#ask what level the user what to play (easy 1-10 medium 1-100 hard 1-1000