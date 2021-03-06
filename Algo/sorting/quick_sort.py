def partion(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partion(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
        
def main():        
    x = [1,64,3,1,3,5,7,89,3221,8,545344]
    quick_sort(x, 0, len(x)-1)
    print (x)

if __name__ == "__main__":
    main()
