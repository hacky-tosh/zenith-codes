n = int(input())
arr = list(map(int, input().split()))

frq = [0]*121
ans= 0
for i in range(n):
    frq[arr[i]] += 1 

for i in range(1,121):
    for j in range(1,121):
        if(i<=j*0.5+7):
            continue 
        if(i>100 and j<100):
            continue
        if(i>j):
            continue
        ans += frq[i]*frq[j]
        if(i==j):
            ans -= frq[i]

print(ans)