import sys
input = sys.stdin.readline
# [BOJ] 10810 공 넣기 / 구현, 시뮬레이션
n, m = map(int, input().split())
busket = [0 for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        busket[i] = c
print(*busket[1:], sep=' ')