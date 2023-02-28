from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 27514 1차원 2048 / 구현, 그리디, 시뮬레이션
n = int(input())
arr = list(map(int, input().split()))

pri_q = []
for i in range(n):
    if arr[i] == 0: continue
    else:
        heappush(pri_q, arr[i])

while len(pri_q) != 2 and len(pri_q) != 1:
    if len(pri_q) == 1: break
    a = heappop(pri_q)
    b = heappop(pri_q)
    if a == b:
        heappush(pri_q, a+b)
    else:
        heappush(pri_q, b)

if len(pri_q) == 1: print(heappop(pri_q))
else:
    v1 = heappop(pri_q)
    v2 = heappop(pri_q)
    if v1 == v2: print(v1+v2)
    else: print(v2)