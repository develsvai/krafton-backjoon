def find_prime_num_count(a: list) -> int:
    count = 0
    for prime in a:
        if prime < 2:
            continue  # 2보다 작은 숫자는 소수가 아니므로 건너뜀
        
        is_prime = True
        for i in range(2, int(prime ** 0.5) + 1):
            if prime % i == 0:
                is_prime = False
                break  # 소수가 아니므로 내부 루프 종료
        
        if is_prime:
            count += 1  # 소수일 때만 count 증가

    return count

# 입력 받기
N = int(input())  # 숫자의 개수
M = list(map(int, input().split()))  # 숫자 리스트

# 소수 개수 계산 및 출력
res = find_prime_num_count(M)
print(res)
