import sys
input = sys.stdin.readline
# [BOJ] 2567 색종이 - 2 / 구현
n = int(input())
paper = [[0 for _ in range(101)] for __ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for r in range(y, y + 10):
        for c in range(x, x+ 10):
            paper[r][c] = 1

count = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                if paper[i + dy][j + dx] == 0:
                    count += 1
    
print(count)