t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    su = 0 
    for i in range(1,n+1):
        su = su + i 
    print(su-sum(li))