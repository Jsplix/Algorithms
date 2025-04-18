import sys
input = sys.stdin.readline
# [BOJ] 15685 드래곤 커브 / 구현, 시뮬레이션
dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]
graph = [[0 for _ in range(101)] for __ in range(101)]
for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    graph[y][x] = 1
    gen = [d]

    for i in range(g):
        for j in range(len(gen)-1, -1, -1):
            gen.append((gen[j] + 1) % 4)
    
    for i in gen:
        nx = x + dir[i][1]
        ny = y + dir[i][0]
        
        if 0 <= nx < 101 and 0 <= ny < 101:
            graph[ny][nx] = 1
            x, y = nx, ny

count = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            count += 1

print(count)