def countingsort(arr,n,k):
    frq = [0]*(k+1)
    for i in range(n):
        frq[arr[i]] += 1 
    count = [0]*(k+1)
    count[0] = frq[0] 
    for i in range(1,k):
        count[i] = count[i-1] + frq[i]
    
    brr = [None]*n 
    for i in range(n-1,-1,-1):
        count[arr[i]] -= 1 
        brr[count[arr[i]]] = arr[i]
    
    return brr 

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    max = -1 
    for i in range(n):
        if(max<arr[i]):
            max = arr[i]
    k = max
    arr = countingsort(arr, n, k)
    print(*arr)
    




if __name__=='__main__':
    main()