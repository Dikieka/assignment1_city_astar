import heapq
import math
import time  

def euclidean(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def a_star(cities, roads, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g = {city: float('inf') for city in cities}
    g[start] = 0
    f = {city: float('inf') for city in cities}
    f[start] = euclidean(cities[start], cities[goal])

    node_count = 1  

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct(came_from, start, goal), node_count

        for neighbor in roads[current]:
            temp_g = g[current] + euclidean(cities[current], cities[neighbor])
            if temp_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = temp_g
                f[neighbor] = temp_g + euclidean(cities[neighbor], cities[goal])
                heapq.heappush(open_set, (f[neighbor], neighbor))
                node_count += 1  
    return None, node_count

def reconstruct(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path

def run_assignment1():
    cities = {
        "A": (0, 0), "B": (2, 1),
        "C": (4, 2), "D": (5, 5),
        "E": (1, 4)
    }

    roads = {
        "A": ["B", "E"],
        "B": ["A", "C"],
        "C": ["B", "D"],
        "D": ["C"],
        "E": ["A", "D"]
    }

    start, goal = "A", "D"
    
    start_time = time.time()

    path, node_count = a_star(cities, roads, start, goal)
    
    end_time = time.time()
    
    execution_time = (end_time - start_time) * 1000

    print("Assignment 1 - A* Path from A to D:")
    if path:
        print(" -> ".join(path))
    else:
        print("No path found.")
    
    print(f"Execution Time: {execution_time:.4f} ms")
    print(f"Nodes Explored: {node_count}")