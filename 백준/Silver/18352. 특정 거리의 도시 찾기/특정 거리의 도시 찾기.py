import sys
from collections import deque

input = sys.stdin.read

def find_cities_at_distance_k(n, m, k, x, roads):
    graph = [[] for _ in range(n + 1)]
    
    # 간선 정보 입력
    for a, b in roads:
        graph[a].append(b)
    
    # 거리 리스트 초기화
    distance = [-1] * (n + 1)
    distance[x] = 0  # 시작 도시의 거리는 0
    
    # BFS를 위한 큐 초기화
    queue = deque([x])
    
    # BFS 수행
    while queue:
        current_city = queue.popleft()
        
        # 현재 도시와 연결된 모든 도시 탐색
        for next_city in graph[current_city]:
            if distance[next_city] == -1:  # 아직 방문하지 않은 도시
                distance[next_city] = distance[current_city] + 1
                if distance[next_city] == k:
                    queue.append(next_city)
                elif distance[next_city] < k:
                    queue.append(next_city)
    
    # 결과를 저장할 리스트
    result = [i for i in range(1, n + 1) if distance[i] == k]
    
    # 결과 출력
    if result:
        sys.stdout.write("\n".join(map(str, result)) + "\n")
    else:
        sys.stdout.write("-1\n")

# 입력 처리
input_data = input().splitlines()
n, m, k, x = map(int, input_data[0].split())
roads = [tuple(map(int, line.split())) for line in input_data[1:]]

# 함수 실행
find_cities_at_distance_k(n, m, k, x, roads)

