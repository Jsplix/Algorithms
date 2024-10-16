import sys
input = sys.stdin.readline
# [BOJ] 15739 매직스퀘어 / 구현
n = int(input())
mtrx = []
sm = (n * (n**2 + 1)) // 2

col_sum = [0 for _ in range(n)]
row_sum = [0 for _ in range(n)]
diag_sum = [0, 0]
cnt = [0 for _ in range(n**2+1)]
for i in range(n):
    m = list(map(int, input().split()))
    row_sum[i] = sum(m)
    for j in range(n):
        col_sum[j] += m[j]
        cnt[m[j]] += 1
    mtrx.append(m)

    diag_sum[0] += mtrx[i][i]
    diag_sum[1] += mtrx[i][n-1-i]

flag = False
if not (diag_sum[0] == diag_sum[1] == sm):
    flag = True
else:
    for i in range(n):
        if not (col_sum[i] == row_sum[i] == sm): 
            flag = True
            break

if flag: print("FALSE")
else: 
    if cnt[1:].count(0) >= 1: print("FALSE")
    else: print("TRUE")