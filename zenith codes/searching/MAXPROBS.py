n = 6
k = 228 
limit = 240 - k 
sol = 0 
c = 0 
for i in range(1,n+1):
    cursol = limit - sol
    if sol<limit:
        if cursol>sol:
            sol = sol + (i * 5)
            c += 1

print(c)