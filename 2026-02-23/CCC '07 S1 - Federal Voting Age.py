n = int(input())
count = 0
while count < n:
    y = int(input())
    m = int(input())
    d = int(input())
    if y < 1989:
        print("yes")
    elif y > 1989:
        print("no")
    else:
        if m < 2:
            print("yes")
        elif m > 2:
            print("no")
        else:
            if d <= 27:
                print("yes")
            else:
                print("no")
    count += 1