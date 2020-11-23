import math
def bi_search(f, r, arr, key):
    mid = math.floor((f+r)/2)
    if r-f < 0:
        return False
    if arr[mid] == key:
        return True
    elif key < arr[mid]:
        return bi_search(f, mid-1, arr, key)
    else:
        return bi_search(mid+1, r, arr, key)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))