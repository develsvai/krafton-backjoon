def hanoi(n, source, target, auxiliary):
    if n == 1:
        # 원판을 source에서 target으로 옮긴다.
        print(source, target)
        return
    
    # Step 1: n-1개의 원판을 source에서 auxiliary로 옮긴다.
    hanoi(n - 1, source, auxiliary, target)
    
    # Step 2: 가장 큰 원판을 source에서 target으로 옮긴다.
    print(source, target)
    
    # Step 3: n-1개의 원판을 auxiliary에서 target으로 옮긴다.
    hanoi(n - 1, auxiliary, target, source)

# 입력 처리
N = int(input())

# 하노이의 탑 문제 해결 및 출력
print(2 ** N - 1)  # 최소 이동 횟수
if N <= 20:
    hanoi(N, 1, 3, 2)

