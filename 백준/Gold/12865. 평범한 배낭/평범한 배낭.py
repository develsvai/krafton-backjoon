def find_max_weight(v ,w ,k) :

    for i in range(1, len(v)) :
        for j in range(1, k+1) :
            if j >= v[i]:
                #dp[i][j] = max(dp[i][j-v[i]] + w[i],dp[i-1][j])
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v[i]] + w[i])

            else :
                dp [i][j] = dp[i-1][j]

    print(dp[-1][-1])



n,k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
v = [0] * (n + 1)  # n+1 크기의 리스트로 초기화 (인덱스 1부터 사용)
w = [0] * (n + 1)

for i in range(1, n + 1):
    x, y = map(int, input().split())
    v[i] = x
    w[i] = y

find_max_weight(v,w,k)
