import math
def bi_search(f, r, arr, key):
    min_box = math.floor((f+r)/2)
    if f > r:
        return f
    else:
        sum_box = 0
        count_box = 1
        for w in arr:
            if sum_box+w <= min_box:
                sum_box += w        
            else:
                count_box += 1
                sum_box = w
        if count_box <= key:
            return bi_search(f, min_box-1, arr, key)
        else:
            return bi_search(min_box+1, r, arr, key)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(f"Minimum weigth for {k} box(es) = {bi_search(max(arr), sum(arr), arr, k)}")