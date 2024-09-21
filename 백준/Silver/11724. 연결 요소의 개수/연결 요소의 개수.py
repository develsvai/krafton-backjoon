import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for adj in graph[v]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

graph = {i: [] for i in range(1, N + 1)}

index = 2
for _ in range(M):
    u = int(data[index])
    v = int(data[index + 1])
    graph[u].append(v)
    graph[v].append(u)
    index += 2

visited = [False] * (N + 1)
connected_components = 0

for i in range(1, N + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        connected_components += 1

sys.stdout.write(str(connected_components) + '\n')
