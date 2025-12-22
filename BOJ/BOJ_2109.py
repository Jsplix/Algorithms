import sys
import heapq
input = sys.stdin.readline
# [BOJ] 2109 순회강연 / 자료 구조, 그리디, 정렬, 우선순위 큐
n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key= lambda x: (x[1], -x[0]))

pq = []
for p, d in lst:
    heapq.heappush(pq, p)
    if d < len(pq):
        heapq.heappop(pq)

print(sum(pq))