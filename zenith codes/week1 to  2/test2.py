t = int(input())
while(t!=0):
    n = int(input())
    li = list(map(int, input().split()))
    re = []
    for i in range(len(li)-1,-1,-1):
        if li[i]>=max(li[i:len(li)]):
            re.append(li[i])
    print(*re)
    t = t - 1
