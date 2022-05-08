t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    su = 0 
    for i in range(n-1):
        if a[i]>a[i+1]:
            su = su + a[i]
        elif a[i+1]>a[i]:
            su = su + a[i+1]
    print(su)