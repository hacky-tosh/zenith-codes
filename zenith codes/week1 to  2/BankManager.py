t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    while(n!=1):
        for i in range(2,n+1):
            if (n%i==0):
                n = int(n / i )
                c = c + i 
                break
    print(c)