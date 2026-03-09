from asyncio import print_call_graph

b = [10 , "hello", 30 , 20 , 40]
print(b)
print(b[0])
b[1] += 5
print(b[1])
#add a number to the end of the list
b.append(10)
print(b)
b.sort()
print(b)

a = []
a.append(int(input()))
