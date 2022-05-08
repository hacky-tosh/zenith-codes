t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    win = n//2 
    c = 0 
    frq = [0]*n
    for i in range(n):
        frq[a[i]] += 1 
    for i in range(n):
        if frq[i]>win:
            print(i)
            break
    else:
        print(-1)

