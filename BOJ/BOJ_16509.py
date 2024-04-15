import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 16509 장군 / 구현, 그래프 이론, 그래프 탐색, BFS
def OOB(y, x):
    return True if 0 <= y < 10 and 0 <= x < 9 else False

def bfs():
    global r2, c2, board
    queue = deque([(r1, c1, 0)])
    
    dr = [-3, -2, 2, 3, 3, 2, -2, -3]
    dc = [-2, -3, -3, -2, 2, 3, 3, 2]
    chk = {0: (-1, 0), 1: (0, -1), 2: (0, -1), 3: (1, 0), 4: (1, 0), 5: (0, 1), 6: (0, 1), 7: (-1, 0)}
    diag = {0: (-1, -1), 1: (-1, -1), 2: (1, -1), 3: (1, -1), 4: (1, 1), 5: (1, 1), 6: (-1, 1), 7: (-1, 1)}
    while queue:
        r, c, cnt = queue.popleft()

        if r == r2 and c == c2: return cnt
        for i in range(8):
            pr, pc = chk[i][0], chk[i][1]
            if OOB(r + pr, c + pc) and board[r + pr][c + pc] != -1: # 상을 기준으로 동서남북에 왕이 있는지 확인 - 없어야 이동
                ar, ac = diag[i][0], diag[i][1]
                if OOB(r + pr + ar, c + pc + ac) and board[r + pr + ar][c + pc + ac] != -1: # 각 방향에서 대각선에 왕이 있는지 확인 - 없어야 이동
                    nr = r + dr[i]
                    nc = c + dc[i]
                    
                    if OOB(nr, nc) and board[nr][nc] <= 0:
                        if nr == r2 and nc == c2: return cnt + 1
                        board[nr][nc] = board[r][c] + 1
                        queue.append((nr, nc, cnt + 1))

    return -1

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

# 장기판 설정 - 상은 1, 왕은 2로 표현
board = [[0 for _ in range(9)] for __ in range(10)]
board[r1][c1] = 1
board[r2][c2] = -1

print(bfs())