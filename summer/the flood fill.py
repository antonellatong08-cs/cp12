mat = [
    [0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 2, 0],
    [2, 2, 0, 2, 2, 0],
    [0, 2, 2, 2, 0, 0],
    [0, 0, 2, 0, 0, 0],
    [0, 0, 2, 0, 0, 0],
    [0, 2, 2, 0, 0, 0]]

def fill(i, j):
    if j in [len(mat[0]), -1] or i in [len(mat), -1]:
        return
    if mat[i][j] in [1, 2]:
        return
    mat[i][j] = 1
    fill(i, j+1)
    fill(i, j-1)
    fill(i+1, j)
    fill(i-1, j)

fill(0,0)
for row in mat:
    print(*row)