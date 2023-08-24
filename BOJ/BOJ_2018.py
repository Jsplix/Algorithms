import sys
input = sys.stdin.readline
# [BOJ] 2018 수들의 합 5 / 수학, 투 포인터
n = int(input())

sm, cnt = 0, 0
for i in range(1, n+1):
    sm += i
    if ((n - sm) >= 0 and (n-sm) % i == 0): cnt += 1
print(cnt)