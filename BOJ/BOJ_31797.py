import sys
import heapq
input = sys.stdin.readline
# [BOJ] 31797 아~파트 아파트 / 구현, 정렬
n, m = map(int, input().split())
pq = []
for i in range(m):
    h1, h2 = map(int, input().split())
    heapq.heappush(pq, (h1, i+1))
    heapq.heappush(pq, (h2, i+1))

if n % (2*m) == 0: n = 2*m
elif 2*m < n: n %= (2*m)

n -= 1
while n:
    now, who = heapq.heappop(pq)
    n -= 1

print(pq[0][1])