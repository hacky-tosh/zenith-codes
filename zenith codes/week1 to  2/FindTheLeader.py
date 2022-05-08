t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    re = []
    max_ele = 0
    for i in range(len(li)-1,-1,-1):
        if li[i]>=max_ele:
            re.append(li[i])
            max_ele = li[i]
        
    print(*re)
