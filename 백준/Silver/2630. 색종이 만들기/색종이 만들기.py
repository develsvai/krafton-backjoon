def check_color(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                return False
    return True

def count_paper(x, y, n):
    global white, blue
    
    if check_color(x, y, n):
        if paper[x][y] == 0:
            white += 1
        else:
            blue += 1
    else:
        half = n // 2
        count_paper(x, y, half)
        count_paper(x, y + half, half)
        count_paper(x + half, y, half)
        count_paper(x + half, y + half, half)

# 입력 받기
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# 결과를 저장할 변수
white = 0
blue = 0

# 종이 자르기 시작
count_paper(0, 0, N)

# 결과 출력
print(white)
print(blue)
