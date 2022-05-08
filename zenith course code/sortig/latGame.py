


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n-1):
      if i%2==0:
        maxx = max(arr)
        arr.remove(maxx)
      else:
        minn = min(arr)
        arr.remove(minn)
    print(*arr)