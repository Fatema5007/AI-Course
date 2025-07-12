graph = {
    'A': [['B', 'C'], ['D']],  
    'B': [['E']],              
    'C': [],                  
    'D': [['G']],             
    'E': [],                  
    'G': []                    
}


h = {
    'A': 10,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'G': 4
}


solution = {}


solved = {}


def ao_star(node):
    print("Visiting:", node)

    if node in solved and solved[node] == True:
        return
    if len(graph[node]) == 0:
        solved[node] = True
        return

    min_cost = float('inf') 
    best_option = []

    
    for option in graph[node]:
        total = 0
        for child in option:
            total += h[child]
        if total < min_cost:
            min_cost = total
            best_option = option

    if h[node] != min_cost:
        print("Updating heuristic of", node, "from", h[node], "to", min_cost)
        h[node] = min_cost

    solution[node] = best_option

    for child in best_option:
        ao_star(child)

    solved[node] = True  

    for parent in graph:
        for option in graph[parent]:
            if node in option:
               
                if parent not in solved or solved[parent] == False:
                    ao_star(parent)


def print_solution():
    print("\nFinal AO* Solution Path:")
    for node in solution:
        print(node, "->", solution[node])


ao_star('A')      
print_solution()