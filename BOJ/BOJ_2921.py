import sys
input = sys.stdin.readline
# [BOJ] 2921 도미노 / 수학
n = int(input())
result = 0
for i in range(n+1):
    for j in range(i, n+1):
        result += (i + j)

print(result)