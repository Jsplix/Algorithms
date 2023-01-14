import sys
input = sys.stdin.readline
# [BOJ] 1780 종이의 개수 / 재귀, 분할 정복
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = [0, 0, 0] # 차례대로 0, 1, -1의 개수를 저장

def solve(x, y, N):
    num = board[y][x]
    if N == 1:
        result[num] += 1
        return

    for i in range(y, y+N):
        for j in range(x, x+N):
            if num != board[i][j]:
                for p in range(3):
                    for q in range(3):
                        solve(x+N//3*p, y+N//3*q, N//3)
                return
    result[num] += 1

solve(0, 0, n)
print(result[-1], result[0], result[1], sep = '\n')
# 기존의 방식은 시간이 8초 제한 중 7.8초가 걸림.
# https://www.acmicpc.net/source/44866819
# 위의 코드를 참고하여 다시 풀어봄.
# python3으로 채점할 경우 2.6배 (3초) 가량 빨라지고 pypy3로 채점할 경우 10배(0.7초) 가량 빨라짐
# 함수가 호출되고 가장 먼저 실행되는 부분이 해당 분할 구역 시작 지점의 색깔을 확인하고
# 색깔이 다르면, 바로 재귀 함수를 호출하기 때문인듯함.
# 반면, 이전 코드는 일단 if문 3개로 각각의 색깔을 모두 확인했고, N이 0이 되어야 return을 되었기 때문에 더 느린듯함.