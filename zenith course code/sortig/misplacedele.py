t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    crr = sorted(arr)
    c = 0 
    for i in range(n):
        if arr[i]==crr[i]:
            pass 
        else:
            c += 1 
    print(c)


