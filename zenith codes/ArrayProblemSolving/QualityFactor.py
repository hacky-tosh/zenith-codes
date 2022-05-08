n = int(input())
a = list(map(int, input().split()))

qfa = [0]*n

a.sort()
c = 0 
for i in range(n):
    while(qfa[i]!=a[i]):
        if(a[i]<0):
            for j in range(i,n):
                qfa[j] = qfa[j] - 1 
            c = c + 1





print(c)
print(qfa)
    #    if a[i]>0:
    #         for j in range(i,n):
    #             qfa[j] = qfa[j] + 1 
    #         c = c + 1 