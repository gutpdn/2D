def bubbleSort(array):
    n = len(array)
    for p in range(1, n):
        change = False
        for index in range(0, n-p):
            for charpre in array[index]:
                if ord(charpre) >= 65:
                    pre = charpre
            for charcheck in array[index+1]:
                if ord(charcheck) >= 65:
                    nextto = charcheck
            if(pre > nextto):
                array[index], array[index+1] = array[index+1], array[index]
                change = True
        if change == False:
            break
    for item in array:
        print(item, end = ' ')
        
ary = input("Enter Input : ").split()
bubbleSort(ary)
