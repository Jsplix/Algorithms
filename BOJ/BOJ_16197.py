from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 16197 두 동전 / 그래프 탐색, BFS
n, m = map(int, input().split())
board = []
coin_pos = []
for i in range(n):
    board.append(list(input().strip()))
    for j in range(m):
        if board[i][j] == 'o':
            coin_pos.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 동전의 개수는 2개로 고정 -> 동전의 위치를 파악해줌
# 각 동전의 위치에서 동시에 bfs를 실행 -> 같은 방향으로 같이 움직이도록 함. (벽을 만난 경우는 예외지만.)

def bfs(y1, x1, y2, x2, cnt):
    queue = deque([(y1, x1, y2, x2, cnt)])
    while queue:
        p1_y, p1_x, p2_y, p2_x, c = queue.popleft()
        if c >= 10:
            return -1
        for i in range(4):
            nx1 = p1_x + dx[i]
            ny1 = p1_y + dy[i]
            nx2 = p2_x + dx[i]
            ny2 = p2_y + dy[i]
            if 0 <= nx1 < m and 0 <= ny1 < n and 0 <= nx2 < m and 0 <= ny2 < n:
                if board[ny1][nx1] == '#': # 두 번째 동전만 움직임
                    ny1, nx1 = p1_y, p1_x
                if board[ny2][nx2] == '#': # 첫 번째 동전만 움직임
                    ny2, nx2 = p2_y, p2_x
                queue.append((ny1, nx1, ny2, nx2, c + 1))
                # 중복이 생길 수도 있으므로, cnt 값을 변수로 두지 않고 동전의 움직임과 함께 처리되도록
                # 튜플에 같이 넣어서 큐에 저장 및 처리해줌.
            elif 0 <= ny1 < n and 0 <= nx1 < m: # 두 번째 동전이 떨어진 경우
                return c + 1 # 현재 cnt 값에 +1 값을 반환
            elif 0 <= ny2 < n and 0 <= nx2 < m: # 첫 번째 동전이 떨어진 경우
                return c + 1
            else: # 모두 떨어진 경우
                continue # 다시 확인
    return -1 # 최종적으로 떨어지지 못한 경우 -1 반환

print(bfs(coin_pos[0][0], coin_pos[0][1], coin_pos[1][0], coin_pos[1][1], 0))

# cnt >= 10에서 등호를 붙이지 않으면 아래의 케이스에서 11을 반환. (중복 확인이 안되서 그런 듯함.)
# 7 6
# ######
# ##o..#
# ####.#
# #o##.#
# ####.#
# .....#
# ######