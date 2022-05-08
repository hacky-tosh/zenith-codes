t= int(input())
while(t>0):
  n = int(input())
  arr = list(map(int, input().split()))
  k = int(input())
  i = 0 
  j = n-1
  f = 0
  while(i<j):
      su = arr[i]+arr[j]
      if(su==k):
          f = 1 
          print(i,j)
          break
      elif(su>k):
          j = j - 1
      else:
           i = i + 1 
  if(f==0):
      print('no answer') 
  t = t - 1







      
