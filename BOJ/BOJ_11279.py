import sys
import heapq
# [BOJ] 11279 최대힙 / heap, priority queue
input = sys.stdin.readline
arr = []
n = int(input())
for _ in range(n):
    e = int(input())
    if e == 0:
        if arr != []:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, (-e, e)) # 우선순위를 이용하여 최대 큐를 뽑아냄