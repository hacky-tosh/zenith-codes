t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    re = []
    for i in range(0,len(li)):
        if i==0:
            if li[i]>li[i+1]:
                re.append(i)

        elif i==len(li)-1:
            if li[i]>li[i-1]:
                re.append(i)
        else:
            a = li[i-1]
            x = li[i]
            b = li[i+1]
            if x>a and x>b:
                re.append(i)
    if len(re)>0:
        print(*re)
    else:
        print(-1)

                

          