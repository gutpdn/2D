class Graph:

  def __init__(self, graphList):
    self.weight = dict()
    for node in graphList:
      self.weight[node] = []

  def edge(self, prede, suc, weight = 1):
    if suc not in self.weight[prede]:
      self.weight[prede].append(suc)
      self.weight[suc].append(prede)
    
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

  def dfs(self, vertex, visited = []):
    if vertex not in visited:
      print(vertex, end = ' ')
      visited.append(vertex)
    for node in self.weight[vertex]:
      if node not in visited:
        self.dfs(node, visited)

  def bfs(self):
    visited = []
    for vertex in self.weight:
      if vertex not in visited:
        print(vertex, end = ' ')
        visited.append(vertex)
      for s in self.weight[vertex]:
        if s not in visited:
          print(s, end = ' ')
          visited.append(s)
              
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
print('Depth First Traversals : ',end = '')
for i in vertex_lst:
  g.dfs(i)
print('\nBredth First Traversals : ',end = '')
g.bfs()      
