t = int(input())

for _ in range(t):
    n = int(input())
    lis = [int(x) for x in str(n)]
    lis.sort()
    c = 0 
    start = lis[0]
    for i in range(len(lis)-1):
        if lis[i+1]-lis[i]==1:
            c = c + 1 
    if c+1 == len(lis):
        print("YES")
    else:
        print("NO")