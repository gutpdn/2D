def bubbleSort(array):
    n = len(array)
    for p in range(1, n):
        changed = False
        for index in range(0, n-p):
            if(array[index] > array[index+1]):
                array[index], array[index+1] = array[index+1], array[index]
                changed = True
        if changed == False:
            break
    return array
    
def listSort(listArray):
    n = len(listArray)
    for p in range(1, n):
        listChanged = False
        for index in range(0, n-p):
            if(len(listArray[index]) > len(listArray[index+1])):
                listArray[index], listArray[index+1] = listArray[index+1], listArray[index]
                listChanged = True
        if listChanged == False:
            break
    for item in listArray:
        print(item)

def subset_sum(target, lst, left=0, res=[], carry=[]):  # knapsack style
    if left >= len(lst):
        return res
    carry.append(lst[left])
    if sum(carry) == target:
        res.append(carry.copy())
    res = subset_sum(target, lst, left+1, res, carry)
    carry.pop()
    res = subset_sum(target, lst, left+1, res, carry)
    return res

ary = input("Enter Input : ").split('/')
target = int(ary[0])
ary1 = list(map(int, ary[1].split()))
sumAry = subset_sum(target, bubbleSort(ary1))
if len(sumAry) is 0:
    print("No Subset")
else:
    listSort(sumAry)