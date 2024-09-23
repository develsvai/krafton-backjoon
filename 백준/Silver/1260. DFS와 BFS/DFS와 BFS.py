from collections import deque, defaultdict

def dfs(graph, start):
    stack = [start]
    visited = set()  # 방문한 정점을 기록할 set

    while stack:
        node = stack.pop()

        if node not in visited:  # 방문한 적이 없는 경우에만 실행
            visited.add(node)
            print(node, end=' ')  # 방문한 노드 출력

            # 인접 노드를 스택에 추가 (역순으로 추가해서 작은 번호부터 pop)
            for adj in reversed(graph[node]):  # 여기서 정점 리스트는 역순으로 탐색
                if adj not in visited:
                    stack.append(adj)

    print()  # 출력이 끝난 후 개행


def bfs(graph, start):
    queue = deque([start])
    visited = {start: True}  # 방문한 정점을 기록할 dict (True/False)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')  # 방문한 노드 출력

        for adj in graph[vertex]:
            if adj not in visited:
                queue.append(adj)
                visited[adj] = True  # 방문 처리

    print()  # 출력이 끝난 후 개행


n, m, v = map(int, input().split())
graph = defaultdict(list)  # 디폴트 리스트로 그래프 초기화

# 간선 정보 입력
for _ in range(m):
    u, w = map(int, input().split())
    graph[u].append(w)
    graph[w].append(u)

# 각 정점의 인접 리스트 정렬 (오름차순)
for node in graph:
    graph[node].sort()

# DFS와 BFS 실행
dfs(graph, v)
bfs(graph, v)
