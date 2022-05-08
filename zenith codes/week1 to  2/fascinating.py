def checkF(n):
    n = n + 1
    while(len(str(n))!=len(set(map(int,str(n))))):
        n = n + 1

    return n 


t = int(input())
for _ in range(t):
    n = int(input())
    print(checkF(n))


