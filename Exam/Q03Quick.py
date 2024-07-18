#3 Divide and Conquer O(nlogn)
def partition(arr,low,high):
    pivot = arr[low]
    i=low+1
    for j in range(low+1,high+1):
        if arr[j]<=pivot:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
    arr[i-1], arr[low] = arr[low], arr[i-1]
    return i-1

def quicksort(arr,low,high):
    if low<high:
        pi = partition(arr, low, high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
arr = [5,6,7,8,1]
(quicksort(arr,0,4))
print(arr)