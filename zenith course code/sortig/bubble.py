def bubblesort(a,n):
    for i in range(0,n):
        swapped = 0
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swapped += 1
        if swapped==0:
            break


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print("Array before sorting : ")
    print(*arr)
    bubblesort(arr, n)
    print("Array after sorting : ")
    print(*arr)

if __name__=='__main__':
    main()

