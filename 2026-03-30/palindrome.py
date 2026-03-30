#p = input()
#length = len(p)
#palindrome = True
#for i in range(length):
#    if p[i] != p[length-i-1]:
#        palindrome = False
#        break
#if palindrome == True:
#    print("yes")
#else:
#    print("no")

#string sclicing
#s = "abcdefghij"
#     0123456789
#print(s[3 : 8 : 2])
#print(s[8 : 3]) get nothing
#print(s[8 : 3 : -1]) get things backward
#print(s[:8]) get from a
#print(s[5 :]) get to the last one
#print(s[ : : 2]) remember this one

p = input()
length = len(p)
if p == p[::-1]:
    print("yes")
else:
    print("no")