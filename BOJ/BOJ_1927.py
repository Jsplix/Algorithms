import sys
import heapq
input = sys.stdin.readline
# [BOJ] 1927 최소 힙 / 자료구조, 우선순위 큐
n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if arr != []:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, x)