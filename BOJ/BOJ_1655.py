import sys
import heapq
input = sys.stdin.readline
# [BOJ] 1655 가운데를 말해요 / 자료 구조, 우선순위 큐
N = int(input())

left_heap, right_heap = [], []
result = []
for i in range(N):
    x = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x)
    else:
        heapq.heappush(right_heap, x)
    
    if left_heap and right_heap:
        if -left_heap[0] > right_heap[0]:
            temp = -heapq.heappop(left_heap)
            heapq.heappush(left_heap, -heapq.heappop(right_heap))
            heapq.heappush(right_heap, temp)
    
    result.append(-left_heap[0])
print('\n'.join(map(str, result)))