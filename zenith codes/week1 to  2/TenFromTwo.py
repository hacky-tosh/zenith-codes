t = int(input())

for _ in range(t):
    n = int(input())
    c = 0 
    if n%5==n and n%10==n:
        print(-1)
    else:
        while(n%10!=0):
            n = n * 2 
            c = c + 1 
        print(c)