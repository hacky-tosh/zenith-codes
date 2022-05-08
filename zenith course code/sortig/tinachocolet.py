t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    tina = 0 
    rahul = 0
    for i in range(n):
      if i%2==0:
        maxx = max(arr)
        tina = tina + maxx
        arr.remove(maxx)
      else:
        maxx = max(arr)
        rahul = rahul + maxx
        arr.remove(maxx)
    print(tina)