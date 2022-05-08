n = 6 
k = 6
a = [1,3,1,10,2,9]

c = 0 
f = a[0]
l = a[n-1]
i = 0 
c = 0 
while(f<=k or l<=k):
    if i>n:
        break
    if a[i]<=k: 
        if f<=k:
            a.remove(a[i])
            print(c,i,a,a[i])        
            c = c + 1 
        if l<=k:
            a.remove(a[n-1-i])
            c = c + 1 
    i = i + 1 
print(c)
print(a)


        
