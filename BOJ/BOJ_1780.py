import sys
input = sys.stdin.readline
# [BOJ] 1780 종이의 개수 / 분할 정복, 재귀
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0


def solve(x, y, N):
    global minus_cnt, zero_cnt, plus_cnt
    
    if N == 0: return 0
    
    minus_temp, zero_temp, plus_temp = 0, 0, 0

    for i in range(y, y+N):
        for j in range(x, x+N):
            if board[i][j] == -1:
                minus_temp += 1
            elif board[i][j] == 0:
                zero_temp += 1
            elif board[i][j] == 1:
                plus_temp += 1

    if (minus_temp or zero_temp or plus_temp) == N**2:
        if minus_temp: minus_cnt += 1
        if zero_temp: zero_cnt += 1
        if plus_temp: plus_cnt += 1
    else:
        solve(x, y, N//3)
        solve(x+N//3, y, N//3)
        solve(x+(2*N)//3, y, N//3)
        solve(x, y+N//3, N//3)
        solve(x+N//3, y+N//3, N//3)
        solve(x+(2*N)//3, y+N//3, N//3)
        solve(x, y+(2*N)//3, N//3)
        solve(x+N//3, y+(2*N)//3, N//3)
        solve(x+(2*N)//3, y+(2*N)//3, N//3)
    return

x, y, z = 0, 0, 0
for i in range(n):
    x += board[i].count(-1)
    y += board[i].count(0)
    z += board[i].count(1)
if (x or y or z) == n**2:
    if x: minus_cnt += 1
    if y: zero_cnt += 1
    if z: plus_cnt += 1
else:
    solve(0, 0, n//3)
    solve(0+n//3, 0, n//3)
    solve(0+(2*n)//3, 0, n//3)
    solve(0, 0+n//3, n//3)
    solve(0+n//3, 0+n//3, n//3)
    solve(0+(2*n)//3, 0+n//3, n//3)
    solve(0, 0+(2*n)//3, n//3)
    solve(0+n//3, 0+(2*n)//3, n//3)
    solve(0+(2*n)//3, 0+(2*n)//3, n//3)
print(minus_cnt, zero_cnt, plus_cnt, sep='\n')