t = int(input())

for _ in range(t):
  st = input()
  ac = 0 
  for ele in st:
    if ele=='a':
      ac = ac + 1
  if ac>len(st)/2:
    print(len(st))
  else:
    print(2*ac-1)