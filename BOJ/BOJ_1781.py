import sys
import heapq
input = sys.stdin.readline
# [BOJ] 1781 컵라면 / 자료 구조, 그리디, 우선순위 큐
n = int(input())
homework = [list(map(int, input().split())) for _ in range(n)]
homework.sort()

pq = []
for deadline, ramen in homework:
    heapq.heappush(pq, ramen)
    if deadline < len(pq):
        heapq.heappop(pq)

print(sum(pq))