class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self, tableSize, maxCol):
        self.tableSize = tableSize
        self.maxCol = maxCol
        self.table = []
        for i in range(tableSize):
            self.table.append(None)
        self.countData = 0

    def addData(self, key, data):
        col = 0
        sum_char = 0
        dataForAdd = Data(key, value)
        for char in key:
            sum_char += ord(char)
        while True:
            index = (sum_char + col*col) % self.tableSize
            if self.countData == len(self.table):
                print("This table is full !!!!!!")
                quit()
            elif self.table[index] is None:
                self.table[index] = dataForAdd
                self.countData += 1
                self.printTable()
                break
            else:
                col += 1
                print(f'collision number {col} at {index}')
                if col >= colMax:               
                    print('Max of collisionChain')
                    self.printTable()
                    break

    def printTable(self):
        for dd in range(len(self.table)):
            print(f"#{dd+1}\t{self.table[dd]}")
        print('---------------------------')

print(" ***** Fun with hashing *****")
inp0, inp1 = input("Enter Input : ").split('/')
table, colMax = map(int, inp0.split())
data = inp1.split(',')
show = hash(table, colMax)
for i in data:
    key, value = i.split()
    show.addData(key, value)