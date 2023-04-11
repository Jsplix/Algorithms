import sys
input = sys.stdin.readline
# [BOJ] 1531 투명 / 구현, 시뮬레이션
n, m = map(int, input().split())
paper_pos = [list(map(int, input().split())) for _ in range(n)]
paper = [[0 for _ in range(100)] for _ in range(100)]

for x1, y1, x2, y2 in paper_pos:
    for i in range(y1-1, y2):
        for j in range(x1-1, x2):
            paper[i][j] += 1

answer = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] > m: answer += 1
print(answer)