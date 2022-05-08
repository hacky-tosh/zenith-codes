def selectionsort(arr,n):
    for i in range(n):
        minInd = i 
        for j in range(i+1,n):
            if arr[minInd]>arr[j]:
                minInd = j 
                minInd = j 
        arr[i],arr[minInd] = arr[minInd],arr[i]


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print("Array before sorting : ")
    print(*arr)
    selectionsort(arr, n)
    print("Array after sorting : ")
    print(*arr)

if __name__=='__main__':
    main()




1 2 3 4 5 6 7 8 