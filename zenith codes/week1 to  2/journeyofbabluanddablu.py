t = int(input())

for _ in range(t):
  n = int(input())
  
  if n%8==2:
    print('{}MB'.format(n+3))
  elif n%8==5:
    print('{}MB'.format(n-3))
  elif n%8==1:
    print('{}LB'.format(n+3))
  elif n%8==4:
    print('{}LB'.format(n-3))
  elif n%8==3:
    print('{}UB'.format(n+3))
  elif n%8==6:
    print('{}UB'.format(n-3))
  elif n%8==7:
    print('{}SU'.format(n+1))
  elif n%8==0:
    print('{}SL'.format(n-1))
