import sys
input = sys.stdin.readline
# [BOJ] 1189 컴백홈 / 그래프 이론, 그래프 탐색, DFS, 백트래킹, 브루트 포스
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

r, c, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]

answer = 0
path = ['a']
def back(idx, x, y):
    global answer
    if len(path) == k and x == c-1 and y == 0:
        answer += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < c and 0 <= ny < r and not visited[ny][nx] and board[ny][nx] != 'T':
            path.append(chr(ord('a')+idx))
            visited[ny][nx] = 1
            back(idx+1, nx, ny)
            path.pop()
            visited[ny][nx] = 0

visited[r-1][0] = 1
back(1, 0, r-1)
print(answer)