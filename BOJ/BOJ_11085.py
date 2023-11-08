from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 11085 군사 이동 / 자료 구조, 그래프 이론, 그래프 탐색, 분리 집합
def find(x):
    if vertex[x] != x: vertex[x] = find(vertex[x])
    return vertex[x]

def union(v1, v2):
    r1, r2 = find(v1), find(v2)
    if r1 < r2: vertex[r2] = r1
    else: vertex[r1] = r2

p, w = map(int, input().split())
c, v = map(int, input().split())

pq = []
vertex = [i for i in range(p)]
for _ in range(w):
    start, end, width = map(int, input().split())
    heappush(pq, (-width, start, end))

while pq:
    weight, s, e = heappop(pq)
    weight *= -1
    union(s, e)

    if find(c) == find(v):
        answer = weight
        break

print(answer)