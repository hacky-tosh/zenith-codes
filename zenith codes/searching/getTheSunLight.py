t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 1  
    maxx = a[0]
    for i in range(1,n):
        if maxx<a[i]:
            ans = ans + 1
            maxx = a[i]
    print(ans)


  