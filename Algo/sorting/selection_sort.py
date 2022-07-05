# Time complexity :  O(n**2) : n is the length of the array

def selec_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def main():
    x = [7,8,9,1,2,3,4,76,5,6]
    selec_sort(x)
    print (x)

if __name__ == "__main__":
    main()
