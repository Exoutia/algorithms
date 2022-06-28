# Time complexity :  O(n**2) : n is the length of the array

def bub_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


x = [7,8,9,1,2,3,4,76,5,6]
bub_sort(x)
print (x)