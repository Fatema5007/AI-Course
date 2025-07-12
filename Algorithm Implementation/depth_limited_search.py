graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':['H','I'],
    'E':['J','K'], 
    'F':['L','M'],
    'G':['N','O'],
    'H':[],
    'I':[],
    'J':[],
    'K':[],
    'L':[],
    'M':[],
    'N':[],
    'O':[]
}

level1=0
path_not =[]


def DLS(start,goal,path,level,maxD):
  global level1
  global path_not
  
  print('\nCurrent level-->',level)
  print('Goal node testing for',start)
  path.append(start)
  if start == goal:
    print("Goal test successful")
    return path
  print('Goal node testing failed')
  if level==maxD:
    level1=level
    path_not=path
    path.pop()
    return False
    
  print('\nExpanding the current node',start)
  for child in graph[start]:
    if DLS(child,goal,path,level+1,maxD):
       return path
    
  return False
  
  
  
start = 'A'
goal = input('Enter the goal node:-')
maxD = int(input("Enter the maximum depth limit:-"))

path = list()
res = DLS(start,goal,path,0,maxD)

if res:
    print("Path to goal node available")
    print("Path is :",res)
    
else:
    print("No path available within the given depth")
    print("The level at which the goal node is not found:",level1)
    print("The path it has visited but not found the goal :",path_not)