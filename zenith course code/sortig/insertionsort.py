def insertionsort(arr,n):
    for i in range(1,n):
        temp =  arr[i]
        j = i - 1
        while(j>-1 and arr[j]>temp):
            arr[j+1] = arr[j]
            j = j - 1 
        arr[j+1] = temp




def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print("Array before sorting : ")
    print(*arr)
    insertionsort(arr, n)
    print("Array after sorting : ")
    print(*arr)

if __name__=='__main__':
    main()
