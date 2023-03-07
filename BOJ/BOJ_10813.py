import sys
input = sys.stdin.readline
# [BOJ] 10813 공 바꾸기 / 구현, 시뮬레이션
n, m = map(int, input().split())
basket = [i for i in range(n+1)]
exchange = [tuple(map(int, input().split())) for _ in range(m)]

for e1, e2 in exchange:
    basket[e1], basket[e2] = basket[e2], basket[e1]

print(*basket[1:])