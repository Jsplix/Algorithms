import sys
input = sys.stdin.readline
# [BOJ] 15489 파스칼 삼각형 / 수학, DP, 조합론
pascal = [[0 for _ in range(31)] for _ in range(31)]
for i in range(1, 31):
    pascal[i][1] = 1

for i in range(2, 31):
    for j in range(2, 31):
        pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]

r, c, w = map(int, input().split())
sm = 0
for i in range(w):
    for j in range(i+1):
        sm += pascal[r+i][c+j]
print(sm)