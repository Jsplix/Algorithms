from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 2206 벽 부수고 이동하기 / 그래프 이론, 그래프 탐색, BFS
# 이 문제는 모든 1을 1개씩 부수는 경우 O(N*M*(1의 개수))의 시간 복잡도를 가짐.
# N과 M이 1000이고 1의 개수가 998일 경우 9억 9천 8백만의 연산을 하게 되므로 2초의 시간으로 턱없이 부족함.
# 따라서, 벽을 부쉈을 때의 visited와 부수지 않았을 때의 visited를 구분하여 구함.
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
MAX = 10**6 + 1
def bfs(pos_x, pos_y, cnt, b_cnt):
    global visited

    queue = deque([(pos_x, pos_y, cnt, b_cnt)])
    visited[b_cnt][pos_y][pos_x] = 1

    while queue:
        x, y, cnt, b_cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == m-1 and ny == n-1: return cnt+1
            # b_cnt값에 맞게 visited를 갱신해줌
            if 0 <= nx < m and 0 <= ny < n and not visited[b_cnt][ny][nx] and mtrx[ny][nx] == 0 and (b_cnt == 1 or b_cnt == 0):
                queue.append((nx, ny, cnt+1, b_cnt))
                visited[b_cnt][ny][nx] = 1
            if 0 <= nx < m and 0 <= ny < n and not visited[b_cnt][ny][nx] and mtrx[ny][nx] == 1 and b_cnt == 0:
                queue.append((nx, ny, cnt+1, b_cnt+1))
                visited[b_cnt+1][ny][nx]
    return MAX

n, m = map(int, input().split())
mtrx = [list(map(int, input().rstrip())) for _ in range(n)]

if n == m == 1:
    if mtrx[0][0] == 0: print(1)
    else: print(-1)
    exit(0)

visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)] # [i][j][k] -> [i: 0~1] => 0: 안부숨 / 1: 부숨
mn = bfs(0, 0, 1, 0)

if mn == MAX: print(-1)
else: print(mn)