def bubbleSort(array):
    n = len(array)
    for p in range(1, n):
        show = "None"
        change = False
        for index in range(0, n-p):
            nextindex = 1
            if array[index] < 0:
                continue
            while array[index+nextindex] < 0:
                nextindex += 1
                if index+nextindex > n-1:
                    break
            if index+nextindex > n-1:
                    continue
            if array[index] > array[index+nextindex]:
                array[index], array[index+nextindex] = array[index+nextindex], array[index]
                show = str(array[index+nextindex])
                change = True
        if change == False:
            break
    return array
ary = list(map(int,input("Enter Input : ").split()))
out = bubbleSort(ary)
for item in out:
    print(item, end = ' ')