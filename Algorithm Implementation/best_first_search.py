def best_first_search(graph, start, goal, heuristic):
    def get_heuristic(node):
        return heuristic[node]

    visited = set()
    queue = [start]
    path = {}

    while queue:
       
        current = min(queue, key=get_heuristic)
        queue.remove(current)

        if current == goal:
            return build_path(path, start, goal)

        if current in visited:
            continue
        
        visited.add(current)
       

  
        if current in graph:
            neighbors = graph[current]
        else:
            neighbors = []

        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in queue:
                path[neighbor] = current
                queue.append(neighbor)

    return None


def build_path(path, start, goal):
    current = goal
    result = []

    while current != start:
        result.append(current)
        current = path[current]

    result.append(start)
    result.reverse()
    return result


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 5,
    'G': 0
}


start_node = 'A'
goal_node = 'G'
result_path = best_first_search(graph, start_node, goal_node, heuristic)

print("Path found:", result_path)