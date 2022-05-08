t = int(input())

while(t>0):
    n = int(input())
    a = list(map(int, input().split()))
    re = [] 
 
    for i in range(n):
        if a[n-1-i] not in re:
            re.append(a[n-1-i])
        if a[i] not in re:
            re.append(a[i])
    print(*re)



    t = t - 1