numbers = []

for _ in range(4):
    numbers.append(int(input()))


row_sums = [sum(row) for row in numbers]

col_sums = []
for col in range(4):
    col_sum = 0
    for row in range(4):
        col_sum += numbers[row][col]
    col_sums.append(col_sum)


if row_sums == col_sums == 34:
    print("magic")
else:
    print("not magic")