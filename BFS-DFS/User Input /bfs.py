graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbours = input(f"Enter neighbours of {node} separated by space: ").split()
    graph[node] = neighbours

start = input("Enter starting node: ")

visited = []
queue = []

def bfs(start):
    visited.append(start)
    queue.append(start)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS Traversal:")
bfs(start)
