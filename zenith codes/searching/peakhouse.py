t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0 
    for i in range(1,n-1):
        mid = a[i]
        if mid>a[i+1] and mid>a[i-1]:
            c = i
    if c==0:
        if a[n-1]>a[n-2]:
            print(n-1)
    else:
        print(c)

