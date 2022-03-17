from collections import deque

def shortest_path(edges, node_A, node_B):
    graph = create_adj_graph(edges)
    
    queue = deque()
    queue.append((node_A, 0))
    
    while queue:
        curr, distVal = queue.popleft()
        if curr == node_B:
            return distVal
        neighbors = graph[curr]
        for neighbor in neighbors:
            queue.append((neighbor, distVal+1))
    
    return -1

def create_adj_graph(edges):
    graph = {}
  
    for edge in edges:
        pointA, pointB = edge
        print(pointA, pointB)
        if pointA not in graph: graph[pointA] = []
        if pointB not in graph: graph[pointB] = []
        graph[pointA].append(pointB)
        graph[pointB].append(pointA)
    print(graph)
    return graph


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z')) # -> 2