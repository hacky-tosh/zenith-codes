def zigzag(arr,n,start):
    re = 0
    for i in range(start,n,2):
        temp = arr[i]
        if(i):
           temp = min(temp, arr[i-1]-1)
        if(i+1 != n):
           temp = min(temp,arr[i+1]-1)
        re += arr[i] - temp
    return re 




n = int(input())
arr = list(map(int, input().split()))
re1 = zigzag(arr, n, 0)
re2 = zigzag(arr, n, 1)
if re1<re2:
    print(re1)
else:
    print(re2)