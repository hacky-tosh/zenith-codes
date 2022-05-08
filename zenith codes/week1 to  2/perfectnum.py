t = int(input())

for _ in range(t):
    n = int(input())
    a = []
    for i in range(1,n):
        if n%i==0:
            a.append(i)
    if sum(a)==n:
        print('true')
    else:
        print('false')
