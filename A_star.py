import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h  # Total cost
    
    def __lt__(self, other):  # Fix comparison for heapq
        return self.f < other.f

    @staticmethod
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def astar(grid, start, goal):
    open_list = []
    start_node = Node(start, None, 0, Node.heuristic(start, goal))
    heapq.heappush(open_list, start_node)
    closed_list = set()
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        closed_list.add(current_node.position)
        
        for dx, dy in directions:
            neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)
            
            # Check bounds and obstacles
            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and  # Check if walkable
                neighbor_pos not in closed_list):

                g_cost = current_node.g + 1  # Assume uniform cost
                h_cost = Node.heuristic(neighbor_pos, goal)
                neighbor_node = Node(neighbor_pos, current_node, g_cost, h_cost)

                heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Example grid (0 = walkable, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)
print("Path:", path)
