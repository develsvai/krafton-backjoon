import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기

def merge_sort(arr, start, end):
    if end - start <= 1:
        return

    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid, end)
    merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    i, j, k = 0, 0, start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# 입력 받기
N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

# 합병 정렬 실행
merge_sort(numbers, 0, N)

# 결과 출력
for num in numbers:
    sys.stdout.write(str(num) + '\n')