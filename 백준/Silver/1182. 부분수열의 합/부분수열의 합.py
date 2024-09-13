original = 0  # 부분수열의 합이 S가 되는 경우의 수를 저장할 변수
arr = []  # 입력받은 수열을 저장할 리스트

def find_subsequence(index, current_sum):
    global original  # 함수 외부의 'original' 변수를 사용하기 위해 global로 선언

    # 수열의 끝에 도달한 경우
    if index == len(arr):
        # 현재 부분수열의 합이 S와 같으면 경우의 수 증가
        if current_sum == S:
            original += 1
        return

    # 현재 원소를 포함하는 경우
    find_subsequence(index + 1, current_sum + arr[index])

    # 현재 원소를 포함하지 않는 경우
    find_subsequence(index + 1, current_sum)

# 입력 처리


num = list(map(int, input().split()))

N = num[0]
S = num[1]

# N개의 정수를 공백으로 구분하여 입력받기
arr = list(map(int, input().split()))
if len(arr) != N:
    print()
else:
    # 재귀 호출을 시작
    find_subsequence(0, 0)

    # S가 0일 때 공집합인 경우는 제외
    if S == 0:
        original -= 1

    print(original)
