import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 14442 벽 부수고 이동하기 2 / 그래프 이론, 그래프 탐색, BFS

# PyPy3로 제출, visited를 벽 부순 횟수에 따른 3차원 배열로 생각하기. 
# visited를 해당 문제와 같이 설정해야하는 문제는 몇 번 풀어봤지만 익숙하지 않은데. 앞으로는 익숙해질 것.

def OOB(x, y): # 경계를 벗어나는지 확인. 
    global n, m, k
    if x < 0 or x >= m or y < 0 or y >= n: return True
    return False

def BFS():
    global n, m, k
    queue = deque([(0, 0, k, 1)])
    # 벽 부순 횟수에 따른 3차원 visited 배열.
    visited = [[[0 for _ in range(m)] for __ in range(n)] for _ in range(k+1)] 
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while queue:
        x, y, c, cnt = queue.popleft()
        if x == m-1 and y == n-1: return cnt # 반례에 따른 예외 처리 / 1 1 0 - 0 → output: -1, answer = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not OOB(nx, ny):
                # 벽 부수고 이동하는 경우.
                if c and board[ny][nx] == 1 and not visited[c-1][ny][nx]:
                    visited[c-1][ny][nx] = 1
                    queue.append((nx, ny, c-1, cnt+1))
                # 그냥 이동 가능한 경우
                if board[ny][nx] == 0 and not visited[c][ny][nx]:
                    if nx == m-1 and ny == n-1: return cnt + 1 # 목적지 도달한 경우. cnt값 반환
                    visited[c][ny][nx] = 1
                    queue.append((nx, ny, c, cnt+1))

    return -1 # 목적지까지 도달하지 못한 경우

n, m, k = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
print(BFS()) # return 값 출력