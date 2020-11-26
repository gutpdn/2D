class Graph:
  def __init__(self, graphList):
    self.weight = dict()
    for node in graphList:
      self.weight[node] = []

  def edge(self, prede, suc, weight = 1):
    if suc not in self.weight[prede]:
      self.weight[prede].append(suc)
      #self.weight[suc].append(prede)
    
  def graphInArray(self):
    print(f'    ', end = '')
    for node in self.weight:
      print(node, end = '  ')
    print()
    for node in self.weight:
      i = 0
      print(f"{node} : ", end = '')
      for check in self.weight:
        found = False
        for item in self.weight[node]:
          if item is check:
            found = True
            break
        i += 1
        if found == True:
          print('1', end = '')
        else:
          print('0', end = '')
        if i < len(self.weight):
          print(', ', end='')
      print()

lst = input("Enter : ").split(',')
vertex_lst = []
for data in lst:
  src, dest = data.split()
  if src not in vertex_lst:
    vertex_lst.append(src)
  if dest not in vertex_lst:
    vertex_lst.append(dest)
  vertex_lst = sorted(vertex_lst)

g = Graph(vertex_lst)
for data in lst:
  src, dest = data.split()
  g.edge(src, dest)
g.graphInArray()
