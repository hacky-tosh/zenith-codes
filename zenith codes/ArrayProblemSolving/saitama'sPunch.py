t = int(input())

while(t>0):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  ans = 0
  t = k
  for i in range(n):
      x = a[i]
      ans = ans + k  
