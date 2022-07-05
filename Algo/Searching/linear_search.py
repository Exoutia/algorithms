def lin_search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

def main():
    num = [23,4,3214325,543,212,345345,53,13578,645,43562231,35]
    print(lin_search(num, len(num), 543))

if __name__=='__main__':
    main()