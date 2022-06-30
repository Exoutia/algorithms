import math
def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n)-1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
        # print(prev, step)
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1

def main():
    arr = [-9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 78, 87, 98, 6532, 543211]
    x = -9
    print(jump_search(arr, x))
    
if __name__ == "__main__":
    main()