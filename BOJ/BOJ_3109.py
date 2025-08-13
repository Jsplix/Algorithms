import sys
input = sys.stdin.readline
# [BOJ] 3109 빵집 / 그래프 이론, 그래프 탐색, DFS, 격자 그래프, 그리디 
def back(depth, pr, pc):
    global r, c, result
    if depth == c - 1:
        graph[pr][pc] = 'x'
        result += 1
        return True

    for i in range(3):
        nr = pr + dr[i]
        nc = pc + dc[i]
        if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] == '.':
            ret = back(depth + 1, nr, nc)
            if ret == False: graph[nr][nc] = '-'
            if graph[nr][nc] == 'x':
                graph[pr][pc] = 'x'
                return True

    return False

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dr = [-1, 0, 1]
dc = [1, 1, 1]

result = 0

for i in range(r):
    back(0, i, 0)

print(result)