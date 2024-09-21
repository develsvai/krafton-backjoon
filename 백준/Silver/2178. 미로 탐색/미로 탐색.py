from collections import deque

# BFS 함수 정의
def bfs(graph, start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 밖으로 나가면 무시
            if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
                continue
            if graph[nx][ny] == 0:
                continue

            # 처음 방문하는 노드라면 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 도착지점의 최단 거리 반환
    return graph[-1][-1]

# 입력 받기
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

print(bfs(graph, 0, 0))
