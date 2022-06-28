def insr_sort(arr:  list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
    return arr
    
x = [7,8,9,1,2,3,4,76,5,6]
insr_sort(x)
print (x)