def max_step_score(v):
    n = len(v)
    
    if n == 0:
        return 0
    elif n == 1:
        return v[0]
    elif n == 2:
        return v[0] + v[1]

    dp = [0] * n
    
    # 초기값 설정
    dp[0] = v[0]
    dp[1] = v[0] + v[1]
    dp[2] = max(v[0] + v[2], v[1] + v[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2] + v[i], dp[i-3] + v[i-1] + v[i])
    
    return dp[-1]



n = int(input())

dp = []
v = [0] * (n + 1)  # n+1 크기의 리스트로 초기화 (인덱스 1부터 사용)

for i in range(1, n + 1):
    x  = int(input())
    v[i] = x

    
res = max_step_score(v)
print(res)



#dp[i]=max(dp[i−2]+계단[i],dp[i−3]+계단[i−1]+계단[i])