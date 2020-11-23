import math
def bi_search(f, r, arr, key, show = None):
    mid = math.floor((f+r)/2)
    if r-f < 0:
        if show is None:
            show = 'No First Greater Value'
        return show
    if arr[mid] == key:
        return arr[mid+1]
    elif key < arr[mid]:
        show = str(arr[mid])
        return bi_search(f, mid-1, arr, key, show)
    else:
        return bi_search(mid+1, r, arr, key, show)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for data in k:
    print(bi_search(0, len(arr) - 1, sorted(arr), data))