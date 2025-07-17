import sys
import heapq
input = sys.stdin.readline
# [BOJ] 2075 N번째 큰 수 / 자료 구조, 정렬, 우선순위 큐
n = int(input())
pq = []
for num in list(map(int, input().split())):
    heapq.heappush(pq, num)

for _ in range(n-1):
    for num in list(map(int, input().split())):
        if pq[0] < num:
            heapq.heappush(pq, num)
            heapq.heappop(pq)

print(pq[0])