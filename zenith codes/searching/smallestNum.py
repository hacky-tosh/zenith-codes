n = int(input())
a = list(map(int, input().split()))
k = int(input())

frq = [0]*n

for i in range(n):
    frq[a[i]] += 1 

for i in range(n):
    if frq[i] == k:
        print(i)
        break