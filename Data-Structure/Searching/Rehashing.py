class hash:
  
    def __init__(self, tableSize, maxCol, threshold):
        self.tableSize = tableSize
        self.maxCol = maxCol
        self.threshold = threshold
        self.table = []
        self.tmpData = []
        for i in range(tableSize):
            self.table.append(None)
        self.countData = 0

    def addData(self, data):
        col = 0
        if data not in self.tmpData:
            print(f"Add : {data}")
            self.countData += 1
        while True:      
            index = (data + col*col) % self.tableSize
            if (self.countData/self.tableSize)*100 > self.threshold:
                print('****** Data over threshold - Rehash !!! ******')
                self.rehashing()
            elif self.table[index] is None:
                self.table[index] = data 
                if data not in self.tmpData:
                    self.tmpData.append(data)
                    self.printTable()
                break
            else:
                col += 1
                print(f'collision number {col} at {index}')
                if col >= colMax:               
                    print('****** Max collision - Rehash !!! ******')
                    col = 0
                    self.rehashing()

    def printTable(self):
        for dd in range(len(self.table)):
            print(f"#{dd+1}\t{self.table[dd]}")
        print('----------------------------------------')

    def rehashing(self):
        self.tableSize = self.get_nearest_prime(self.tableSize)
        self.table = []
        for i in range(self.tableSize):
            self.table.append(None)
        for addnew in self.tmpData:
            self.addData(addnew)

    def get_nearest_prime(self, old_number):
        old_number *= 2
        for num in range(old_number + 1, 2 * old_number):
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                return num

print(" ***** Rehashing *****")
inp0, inp1 = input("Enter Input : ").split('/')
print('Initial Table :')
table, colMax, threshold = map(int, inp0.split())
data = inp1.split()
show = hash(table, colMax, threshold)
show.printTable()
for doto in data:
    show.addData(int(doto))