from collections import deque

# BFS를 사용해 연결된 빙산 덩어리를 세는 함수
def bfs(x, y, visited, grid):
    queue = deque([(x, y)])
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 빙산의 덩어리 개수를 세는 함수
def count_icebergs(grid):
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited, grid)
                count += 1
    
    return count

# 빙산이 녹는 과정을 시뮬레이션하는 함수
def melt_iceberg(grid):
    new_grid = [row[:] for row in grid]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] > 0:
                water_count = 0
                for dx, dy in directions:
                    if grid[i + dx][j + dy] == 0:
                        water_count += 1
                new_grid[i][j] = max(0, grid[i][j] - water_count)
    
    return new_grid

# 메인 함수
def solve():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    year = 0
    while True:
        icebergs = count_icebergs(grid)
        
        if icebergs >= 2:
            print(year)
            return
        
        if icebergs == 0:
            print(0)
            return
        
        grid = melt_iceberg(grid)
        year += 1

# 입력을 받고 해결하는 함수 호출
solve()
