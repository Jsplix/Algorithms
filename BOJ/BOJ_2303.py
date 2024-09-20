import sys
from itertools import combinations
input = sys.stdin.readline
# [BOJ] 2303 숫자 게임 / 구현, 브루트포스
n = int(input())
cards = [list(map(int, input().split())) for _ in range(n)]

check = []
for i in range(n):
    possible = list(combinations(cards[i], 3))
    temp = 0
    for p in possible:
        temp = max(sum(p) % 10, temp)
    check.append((temp, i+1))

check.sort(key=lambda x: (-x[0], -x[1]))
print(check[0][1])