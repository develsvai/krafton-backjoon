def find_H(arr):
    global M

    low = 0
    high = max(arr)  # high는 나무의 최대 높이로 설정해야 함

    while low <= high:
        mid = (low + high) // 2
        sum_of_wood = 0

        # 각 나무에 대해 mid 높이로 자른 후 남은 나무의 길이를 계산
        for height in arr:
            if height > mid:
                sum_of_wood += height - mid

        # 필요한 나무 길이 M보다 많이 가져갔다면, 절단기 높이를 올림
        if sum_of_wood >= M:
            low = mid + 1
        # 필요한 나무 길이 M보다 적게 가져갔다면, 절단기 높이를 내림
        else:
            high = mid - 1

    # high가 최적의 절단기 높이가 됨
    return high

# 입력 받기
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 절단기의 최적 높이 찾기
print(find_H(trees))
