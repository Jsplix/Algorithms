import sys
input = sys.stdin.readline
# [BOJ] 2740 행렬 곱셈 / 수학, 구현, 선형대수학
n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
matrix_b = [list(map(int, input().split())) for _ in range(m)]

ans = [ [0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        for l in range(k):
            ans[i][l] += matrix_a[i][j] * matrix_b[j][l]

# print('\n'.join(map(str, ans)))
for i in range(n):
    print(*ans[i])