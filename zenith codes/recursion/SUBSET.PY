def subsetSums(arr, l, r, sumn=0):
 
    # Print current subset
    if l > r:
        print(sumn, end=" ")
        return
 
    # Subset including arr[l]
    subsetSums(arr, l + 1, r, sumn + arr[l])
 
    # Subset excluding arr[l]
    subsetSums(arr, l + 1, r, sumn)
 
 
# Driver code
arr = [2,4,1,3,6,3,2,6]
n = len(arr)
subsetSums(arr, 0, n - 1)