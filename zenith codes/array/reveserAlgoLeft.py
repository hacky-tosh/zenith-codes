def reveserAlgo(arr,i,j):
    while(i<j):
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1 
     

t = int(input())

while(t>0):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    reveserAlgo(arr, 0, k-1)
    reveserAlgo(arr, k, n-1)
    reveserAlgo(arr, 0, n-1)
    print(*arr)

    t = t - 1