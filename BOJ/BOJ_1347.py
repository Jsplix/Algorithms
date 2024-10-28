import sys
input = sys.stdin.readline
# [BOJ] 1347 미로 만들기 / 구현, 시뮬레이션
n = int(input())
contents = input().rstrip()

graph = [['#' for _ in range(101)] for __ in range(101)]

# 초기 셋팅
sr = sc = er = ec = 50
nr = nc = 50
dir = 2
graph[nr][nc] = '.'

# 0 - 북, 1 - 동, 2 - 남, 3 - 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for c in contents:
    if (c == 'L'):
        dir = (dir + 3) % 4
    elif (c == 'R'):
        dir = (dir + 1) % 4
    else:
        nr += dr[dir]
        nc += dc[dir]
        graph[nr][nc] = '.'

        sr, sc, er, ec = min(sr, nr), min(sc, nc), max(er, nr), max(ec, nc)

for i in range(sr, er+1):
    print(''.join(graph[i][sc:ec+1])) 