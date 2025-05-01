import sys
input = sys.stdin.readline
# [BOJ] 1236 성 지키기 / 구현
r, c = map(int, input().split())
rectangle = [list(input().rstrip()) for _ in range(r)]

row, col = 0, 0
for i in range(r):
    if 'X' not in rectangle[i]: row += 1

for j in range(c):
    if 'X' not in [rectangle[i][j] for i in range(r)]: col += 1

print(max(row, col))