def bi_search(arr, n, x):
    lo = 0
    hi = n - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        print("Mid: ", mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def main():
    num = [23,4,3214325,543,212,345345,53,13578,645,43562231,35]
    num.sort()
    print(bi_search(num, len(num), 53))

if __name__=='__main__':
    main()