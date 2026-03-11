from random import choice
from sys import get_coroutine_origin_tracking_depth

targetword = 'interesting'
target = list(targetword)
print(targetword)
print(target)
user = ["_"] * len(target)
print(user)
if choice in target:
    print("good")
    for i in range (len(target)):
        if target[i] == choice:
            user[i] = choice
    else:
        print("bad")
    print(user)