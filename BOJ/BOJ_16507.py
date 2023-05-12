import sys
input = sys.stdin.readline
# [BOJ] 16507 어두운 건 무서워 / 누적 합
r, c, q = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(r)]
total = [[0 for _ in range(c+1)] for _ in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        total[i][j] = total[i-1][j] + total[i][j-1] - total[i-1][j-1] + picture[i-1][j-1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    area = (r2-r1+1) * (c2-c1+1)
    brightness = total[r2][c2]-total[r2][c1-1]-total[r1-1][c2]+total[r1-1][c1-1]
    print(brightness // area)