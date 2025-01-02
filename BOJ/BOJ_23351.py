import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 23351 물 주기 / 구현, 그리디, 시뮬레이션
n, k, a, b = map(int, input().split())
baskets = deque([k for _ in range(n)])

days = 1
while baskets[0] != 0:
    for i in range(a):
        baskets[0] += b
        baskets.append(baskets.popleft())
    
    for j in range(n):
        baskets[j] -= 1

    days += 1
print(days-1)