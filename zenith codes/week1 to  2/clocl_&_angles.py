n = int(input())

for i in range(n):
  x,y = map(int,input().split())
  re = 11/2*y-30*x
  re = abs(int(re))
  m = 360-re
  if m<re:
      print(m)
  else:
      print(re)

   