#2 Divide and Conquer O(nlogn)
def mergeSort(arr):
    if len(arr)==1:
        return arr
    elif len(arr)==0:
        return arr
    else:
        mid = len(arr)//2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        mergearr = merge(left, right)
        return mergearr
def merge(l,r):
    m = len(l)
    n = len(r)
    i=j=0
    res = []
    while i<m and j<n:
        if l[i]<r[j]:
            res.append(l[i])
            i+=1
        elif l[i]>r[j]:
            res.append(r[j])
            j+=1
        else:
            res.append(l[i])
            i+=1
            j+=1
    res.extend(l[i:])
    res.extend(r[j:])
    return res

n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter the elements: ").split()))
res = mergeSort(arr)
print("Sorted array is: ", res)