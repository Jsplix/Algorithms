import sys
input = sys.stdin.readline
# [BOJ] 16931 겉넓이 구하기 / 구현, 기하학, 3차원 기하학
n, m = map(int, input().split())
paper = [[0 for _ in range(m + 2)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)]  + [[0 for _ in range(m + 2)]]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 2*n*m
for y in range(1, n+1):
    for x in range(1, m+1):
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            area = paper[y][x] - paper[ny][nx]
            if area > 0:
                answer += area

print(answer)