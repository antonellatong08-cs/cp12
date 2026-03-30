N = int(input())
farsentence =""
for i in range(N):
    if i < N-1:
        farsentence += "far,"
    else:
        farsentence += "far"
sentence = "A long time ago in a galaxy " + farsentence + " away..."
print(sentence)

n =int(input())
print("A long time ago in a galaxy " + ", ".join (["far"] * N) + " away...")