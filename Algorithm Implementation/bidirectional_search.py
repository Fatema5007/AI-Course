graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

def bidirectional_search(graph, start, goal):
    
    if start == goal:
        return [start]

   
    start_queue = [start]
    goal_queue = [goal]

    
    start_visited = {start: None}
    goal_visited = {goal: None}

    
    while start_queue and goal_queue:
       
        current_start = start_queue.pop(0)
        for neighbor in graph[current_start]:
            if neighbor not in start_visited:
                start_visited[neighbor] = current_start
                start_queue.append(neighbor)
                if neighbor in goal_visited:
                    return reconstruct_path(start_visited, goal_visited, neighbor)

       
        current_goal = goal_queue.pop(0)
        for neighbor in graph[current_goal]:
            if neighbor not in goal_visited:
                goal_visited[neighbor] = current_goal
                goal_queue.append(neighbor)
                if neighbor in start_visited:
                   
                    return reconstruct_path(start_visited, goal_visited, neighbor)

   
    return None

def reconstruct_path(start_visited, goal_visited, meet_node):
   
    path = []
    node = meet_node 
    print("the meeting node is:", node)
    while node is not None:
        path.append(node)
        node = start_visited[node]
    path.reverse()

    
    node = goal_visited[meet_node]
    while node is not None:
        path.append(node)
        node = goal_visited[node]

    return path


path = bidirectional_search(graph, 'A', 'G')
print("Found path:", path)