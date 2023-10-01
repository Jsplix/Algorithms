from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 19638 센티와 마법의 뿅망치 / 구현, 자료 구조, 우선순위 큐
n, centi_h, t = map(int, input().split())
giant_h = list(int(input()) for _ in range(n))

heap = []
for h in giant_h:
    heappush(heap, (-h, h))

cnt = 0
for i in range(t):
    pri, h = heappop(heap)
   
    if h >= centi_h:
        if h == 1: heappush(heap, (pri, h)); break
        heappush(heap, (-(-pri//2), h//2))
        cnt += 1
    else:
        heappush(heap, (pri, h))
        break

if heap[0][1] < centi_h: 
    print("YES", cnt, sep='\n')
else:
    print("NO", heap[0][1], sep='\n')