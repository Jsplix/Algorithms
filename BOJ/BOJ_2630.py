import sys
input = sys.stdin.readline
# [BOJ] 2630 색종이 만들기 / 분할 정복, 재귀
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
white, blue = 0, 0

def solve(x, y, N):
    global white, blue
    if n == 0:
        return 0
    
    cnt = 0
    for i in range(y, y + N):
        for j in range(x, x + N):
            if board[i][j] == 1:
                cnt += 1
    if not cnt: # 파란색이 없는 경우
        white += 1
    elif cnt == N**2: # 사각형 크기 만큼 파란색이 있는 경우
        blue += 1
    else: # 그 외의 나머지 (파란색이 무작위(?)로 흩어져 있는 경우)
        solve(x, y, N//2)
        solve(x + N//2, y, N//2)
        solve(x, y + N//2, N//2)
        solve(x + N//2, y + N//2, N//2)
    return

solve(0, 0, n)
print(white, blue, sep='\n')