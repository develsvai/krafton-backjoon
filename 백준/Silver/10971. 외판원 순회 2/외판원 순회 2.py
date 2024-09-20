import sys

def tsp(n, W):
    dp = [[None] * n for _ in range(1 << n)]

    def dfs(mask, i):
        if dp[mask][i] is not None:
            return dp[mask][i]
        
        if mask == (1 << n) - 1:
            return W[i][0] if W[i][0] > 0 else sys.maxsize

        min_cost = sys.maxsize
        for j in range(n):
            if mask & (1 << j) == 0 and W[i][j] > 0:
                min_cost = min(min_cost, dfs(mask | (1 << j), j) + W[i][j])
        
        dp[mask][i] = min_cost
        return min_cost

    return dfs(1, 0)

# 입력 받기
n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]

# TSP 해결 및 출력
print(tsp(n, W))
