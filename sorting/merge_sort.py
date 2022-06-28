# Time complexity :  O(nlogn) : n is the length of the array

def merge(arr: list, left: int, right: int, mid: int) -> list:
    i = left
    j = mid
    k = 0
    temp = [0]*(right-left+1)
    while i < mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i < mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    m = 0
    for i in range(left, right + 1):
        arr[i] = temp[m]
        m += 1
    return arr

def merge_sort(arr: list, left: int, right: int) -> list:
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, right, mid+1)
    return arr


x = [7,8,9,1,2,3,4,76,5,6]
merge_sort(x, 0, len(x)-1)
print (x)