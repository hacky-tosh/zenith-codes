n, m = map(int, input().split())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
    

for i in range(0,m):
    for j in range(0,m):
        if i<j:
            print('0',end=' ')
        else:
            print(mat[i][j],end=' ')
    print()

for i in range(0,m):
    for j in range(0,m):
        if i>j:
            print('0',end=' ')
        else:
            print(mat[i][j],end=' ')
    print()