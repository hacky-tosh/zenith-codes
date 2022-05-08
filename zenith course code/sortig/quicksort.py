def partition(arr,low,high):
    x = arr[high]
    i = low - 1 
    for j in range(low,high):
        if arr[j]<=x:
            i = i + 1 
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1




def quickssort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        quickssort(arr, low, pi-1)
        quickssort(arr, pi+1, high)



def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print("Array before sorting : ")
    print(*arr)
    quickssort(arr, 0, n-1)
    print("Array after sorting : ")
    print(*arr)

if __name__=='__main__':
    main()