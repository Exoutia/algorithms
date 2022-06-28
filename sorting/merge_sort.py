# Time complexity :  O(nlogn) : n is the length of the array

def merge(arr: list, left: int, right: int, mid: int) -> list:
    i = left
    j = mid
    k = 0
    temp = [0]*(right-left+1)
    while i < mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]
    return arr