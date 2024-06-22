import sys
input = sys.stdin.readline
# [BOJ] 20002 사과나무 / 브루트포스, 누적 합
n = int(input())
farm = [list(map(int, input().split())) for _ in range(n)]
mx = -1007

accum_sum = [[0 for _ in range(n+1)] for __ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        accum_sum[i][j] = farm[i-1][j-1] + accum_sum[i][j-1] + accum_sum[i-1][j] - accum_sum[i-1][j-1]

for a in range(n): # 정사각형 한 변의 길이 결정
    for r in range(1, n-a+1):
        for c in range(1, n-a+1):
            check = accum_sum[r+a][c+a] - accum_sum[r+a][c-1] - accum_sum[r-1][c+a] + accum_sum[r-1][c-1]
            
            if mx < check:
                mx = check

print(mx)