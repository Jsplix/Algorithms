from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 1987 알파벳 / 그래프 이론, 그래프 탐색, DFS, BFS
r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 0

def bfs():
    global answer
    queue = set([(0, 0, board[0][0])])
    # deque은 시간 초과 발생
    # 같은 위치, 같은 문자열에 대해서 중복을 제거해줌 / fifo의 큐 특성이 사용되지 않아도 됨
    # 어차피, 모든 경우를 완전 탐색하게 되어있음.
    while queue:
        x, y, w = queue.pop()
        answer = max(answer, len(w))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < c and 0 <= ny < r and board[ny][nx] not in w:
                queue.add((nx, ny, w+board[ny][nx]))

bfs()
print(answer)