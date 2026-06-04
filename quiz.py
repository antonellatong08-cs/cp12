mat = [[9, 6, 20],[9, 10, 5]]

ans = 0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] > ans:
            ans = mat[i][j]
print(ans)

temp = max([(row) for row in mat])
print (max(temp))

prices = {'apple': 2
          , 'orange': 3
          , 'banana': 1,
          'mango': 4
          }
ans = 0
for k in prices:
    if prices[k] > ans:
        ans = prices[k]
print(max(prices))
