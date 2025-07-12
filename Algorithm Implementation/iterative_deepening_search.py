graph = {'A':['B','C'],
         'B':['D','E'],
         'C':['G'],
         'D':[],
         'E':['F'],
         'G':[],
         'F':[]
         }

def dfs(currentNode,destination,graph,maxDepth):
    print("Checking for destination",currentNode)
    if currentNode==destination:
        return True
    if maxDepth<=0:
        return False
    for node in graph[currentNode]:
       if dfs(node,destination,graph,maxDepth-1):
           return True
    return False



def iterativeDS(currentNode,destination,graph,maxDepth):
    for i in range(maxDepth):
        if dfs(currentNode,destination,graph,i):
            return True
    return False


if  not iterativeDS('A','E',graph,4):
    print("Path is not available")
else:
    print("A path found")