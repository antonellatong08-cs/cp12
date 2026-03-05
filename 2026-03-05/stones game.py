stones = 7
print("there are seven stones in total, you can take only one or two stones at a time")
while stones > 0:
    player1 = int (input("player1 Enter a number: "))
    stones -= player1
    if stones > 0:
        player2 = int (input("player2 Enter a number: "))
        stones -= player2
        if stones == 0:
            print ("player2 wins")
    else:
        print("player1 wins")
        break

