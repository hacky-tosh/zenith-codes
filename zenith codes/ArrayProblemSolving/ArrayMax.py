t = int(input())

while(t>0):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0 
    for i in range(n):
        su = 0
        x = 0
        for j in range(i,n,k):
            su += arr[j]
            su = max(0, su)
            x = max(x, su)
        ans = max(ans, x)

    print(ans)
    t = t - 1
