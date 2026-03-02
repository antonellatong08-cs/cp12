import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

n = int(input())
even_count = 0
odd_count = 0
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("even number",even_count)
print("odd number",odd_count)

#count the even num and the odd num
