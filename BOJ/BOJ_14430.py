import sys
input = sys.stdin.readline
# [BOJ] 14430 자원 캐기 / DP
n, m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]

val = [[0 for _ in range(m)] for _ in range(n)]
val[0][0] = arr[0][0]
for i in range(n):
    for j in range(m):
        if i == j == 0: continue
        elif i > 0 and j == 0: val[i][j] = val[i-1][j]
        elif i == 0 and j > 0: val[i][j] = val[i][j-1]
        else: val[i][j] = max(val[i-1][j], val[i][j-1])

        if arr[i][j] == 1: val[i][j] += 1

print(max(map(max, val)))