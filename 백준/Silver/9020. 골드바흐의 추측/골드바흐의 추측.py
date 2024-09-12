def isprime(num: int) -> bool:
    # 2보다 작은 수는 소수가 아님
    if num < 2:
        return False
    # 2부터 num의 제곱근까지 나누어 떨어지는지 확인
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def answer(num) :
    length = num //2 

    for temp1 in range(length, 1, -1):
        if(isprime(temp1)):
            if(isprime(num -temp1)) :
                print(str(temp1) + " " + str(num - temp1))
                return
               
    return 1

# N개의 수 입력 받기
N = int(input())

s = []
for _ in range(N):
    s.append(int(input("")))

# 각각의 숫자에 대해 답을 출력
for num in s:
    answer(num)