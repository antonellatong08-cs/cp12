n = int(input())
student = []
correct = []
for i in range(n):
    student.append(input())
for i in range(n):
    correct.append(input())
count = 0
for i in range(n):
    if student[i] == correct[i]:
        count += 1
print(count)