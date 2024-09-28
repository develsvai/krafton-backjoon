import heapq

# 입력 받기
n, k = map(int, input().split())
lab = []
queue = []

# 시험관 정보와 초기 바이러스 위치 입력 받기
for i in range(n):
    row = list(map(int, input().split()))
    lab.append(row)
    for j in range(n):
        if row[j] != 0:
            heapq.heappush(queue, (row[j], 0, i, j))

# S초 후, X, Y 위치 입력 받기
s, x, y = map(int, input().split())

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 실행
while queue:
    next_queue = []
    while queue:
        virus, time, cx, cy = heapq.heappop(queue)
        
        # S초가 지나면 종료
        if time == s:
            break

        # 상하좌우로 바이러스 확산
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 시험관 범위 안에 있고 빈 칸(0)이면 바이러스 확산
            if 0 <= nx < n and 0 <= ny < n and lab[nx][ny] == 0:
                lab[nx][ny] = virus
                next_queue.append((virus, time + 1, nx, ny))
    
    # 다음 초의 확산을 위해 임시 리스트의 모든 요소를 큐에 삽입
    for item in next_queue:
        heapq.heappush(queue, item)

# S초 후의 (X, Y) 위치의 바이러스 출력
print(lab[x-1][y-1])

