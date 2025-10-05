import sys
input = sys.stdin.readline
# [BOJ] 28420 카더가든 / 구현, 브루트포스, 누적 합
N, M = map(int, input().split())
a, b, c = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

acc_sum = [[0 for _ in range(M + 1)] for __ in range(N + 1)]
for i in range(N):
    for j in range(M):
        acc_sum[i + 1][j + 1] = area[i][j] + acc_sum[i + 1][j] + acc_sum[i][j + 1] - acc_sum[i][j]

# 1씩 빼주는 이유 -> 시작 칸을 포함하기 때문에
mn = 10**9
for i in range(1, N + 1 - (a - 1)): # case 1
    for j in range(1, M + 1 - (b + c - 1)):
        temp = acc_sum[i + (a - 1)][j + (b + c - 1)] - acc_sum[i + (a - 1)][j - 1] - acc_sum[i - 1][j + (b + c - 1)] + acc_sum[i - 1][j - 1]
        mn = min(mn, temp)

for i in range(1, N + 1 - (a + b - 1)): # case 2
    for j in range(1, M + 1 - (a + c - 1)):
        temp = acc_sum[i + (a - 1)][j + (c - 1)] - acc_sum[i + (a - 1)][j - 1] - acc_sum[i - 1][j + (c - 1)] + acc_sum[i - 1][j - 1]
        temp += acc_sum[i + (a + b - 1)][j + (c + a - 1)] - acc_sum[i + (a + b - 1)][j + (c - 1)] - acc_sum[i + (a - 1)][j + (c + a - 1)] + acc_sum[i + (a - 1)][j + (c - 1)]
        mn = min(mn, temp)

for i in range(1, N + 1 - (a + c - 1)): # case 3
    for j in range(1, M + 1 - (b + a - 1)):
        temp = acc_sum[i + (a - 1)][j + (b - 1)] - acc_sum[i - 1][j + (b - 1)] - acc_sum[i + (a - 1)][j - 1] + acc_sum[i - 1][j - 1]
        temp += acc_sum[i + (a + c - 1)][j + (b + a - 1)] - acc_sum[i + (a + c - 1)][j + (b - 1)] - acc_sum[i + (a - 1)][j + (b + a - 1)] + acc_sum[i + (a - 1)][j + (b - 1)]
        mn = min(mn, temp)

print(mn)