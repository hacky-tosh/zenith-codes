t = int(input())

for _ in range(t):
    n = int(input())
    
    c =  0
    for i in range(1,len(str(n))):
        c = c + (n - pow(10,i) + 1 )

    print(c+n)
