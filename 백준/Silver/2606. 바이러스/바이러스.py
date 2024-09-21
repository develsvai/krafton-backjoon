import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 0  # 탐색된 노드 수를 세기 위한 변수

    while queue:
        v = queue.popleft()
        count += 1  # 큐에서 꺼낼 때마다 하나의 노드를 방문했다고 간주
        for adj in graph[v]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True

    return count  # 탐색된 노드 수를 반환

# 입력을 받습니다.
N = int(input())  # 정점의 개수
M = int(input())  # 간선의 개수

# 그래프를 인접 리스트로 초기화합니다.
graph = {i: [] for i in range(1, N + 1)}

visited = [False] * (N + 1)

# 간선 정보를 입력받아 그래프에 저장합니다.
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS를 수행하여 1번 컴퓨터를 통해 감염된 컴퓨터 수를 계산합니다.
infected_count = bfs(graph, 1, visited)

# 결과 출력 (1번 컴퓨터를 제외한 감염된 컴퓨터 수)
print(infected_count -1 )