from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 11286 절댓값 힙 / 자료 구조, 우선순위 큐
heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (abs(x), x))