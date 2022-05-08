def rightRotate(arr,n):
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp



k = int(input())
n = int(input())
arr = list(map(int, input().split()))


for i in range(k+1):
    rightRotate(arr,n)
print(*arr)







