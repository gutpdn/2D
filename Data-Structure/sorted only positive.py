def insertionSort(array, n, curr = 1): 
    if curr < n:
        nextItem = array[curr]
        loc = insertionIndex(array, curr, nextItem)
        array[loc] = nextItem
        curr += 1
        if curr < n:
            print(f"insert {nextItem} at index {loc} : {array[:curr]} {array[curr:]}") 
        insertionSort(array, n, curr)
        if curr >= n:
            print(f"insert {nextItem} at index {loc} : {array[:curr]}")
            print(f"sorted\n{array}") 
        
def insertionIndex(array, curr, value):
    if curr > 0 and array[curr-1] > value:
        array[curr] = array[curr-1]
        curr -= 1
        return insertionIndex(array, curr, value)
    else:
        return curr

ary = list(map(int,input("Enter Input : ").split()))
insertionSort(ary, len(ary))