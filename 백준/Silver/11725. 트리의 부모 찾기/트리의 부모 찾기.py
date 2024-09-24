from collections import deque, defaultdict


def find_parents(N, graph):
    # BFS를 위한 큐와 부모를 기록할 배열
    queue = deque([1])
    parents = [0] * (N + 1)  # 부모 노드를 저장할 배열, 인덱스는 노드 번호에 대응

    while queue:
        node = queue.popleft()

        for adj in graph[node]:
            if parents[adj] == 0:  # 아직 부모가 기록되지 않은 경우
                parents[adj] = node  # 부모 기록
                queue.append(adj)  # 큐에 자식 노드 추가

    return parents


# 입력 처리
N = int(input())  # 노드의 수 입력
graph = defaultdict(list)

for _ in range(N - 1):
    u, w = map(int, input().split())
    graph[u].append(w)
    graph[w].append(u)

# 부모 찾기
parents = find_parents(N, graph)

# 2번 노드부터 N번 노드까지 부모 출력
for i in range(2, N + 1):
    print(parents[i])
