n,m  = map(int, input().split())
a = [] 
b = []

for i in range(m):
    x,y = map(int, input().split())
    a.append(x)
    b.append(y)

# [2,3,4,5] 
# [3,4,5,6]

k = 0 
c = 0 
for i in range(m):
    x,y = a[k],b[k]
    for j in range(m):
        if a[j] == x :
            c = c + 1
        elif b[j] == x:
            c = c + 1 
        else:
            k = k + 1 
for i in range(n):
    

