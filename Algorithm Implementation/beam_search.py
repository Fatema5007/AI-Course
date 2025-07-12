def beam_search(graph, start, goal, heuristic, beam_width):
    def get_heuristic(node):
        return heuristic[node]

    visited = set()
    queue = [start]
    path = {}

    while queue:
        
        sorted_queue = sorted(queue, key=get_heuristic)

        
        top_k_nodes = sorted_queue[:beam_width]

       
        queue = top_k_nodes

        next_queue = []

        for current in queue:
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
                if neighbor not in visited and neighbor not in next_queue:
                    path[neighbor] = current
                    next_queue.append(neighbor)

        queue = next_queue

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
beam_width = 1

result_path = beam_search(graph, start_node, goal_node, heuristic,2)
print("Path found:", result_path)