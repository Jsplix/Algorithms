import sys
input = sys.stdin.readline
# [BOJ] 25426 일차함수들 / 수학, 그리디, 정렬
n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
f.sort()

result = 0
for i in range(1, n+1):
    result += f[i-1][0]*i + f[i-1][1]
print(result)