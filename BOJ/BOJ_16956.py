import sys
input = sys.stdin.readline
# [BOJ] 16956 늑대와 양 / 애드 혹, 해 구성하기
r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
flag = False

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if (0 <= ny < r and 0 <= nx < c) and graph[ny][nx] == 'S':
                    flag = True
                    break
        elif graph[i][j] == '.':
            graph[i][j] = 'D'
    if flag: break

if flag: print(0)
else: 
    print(1)
    for gph in graph:
        print(''.join(gph))