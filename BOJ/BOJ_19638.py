from heapq import heapify, heapreplace
import sys
input = sys.stdin.readline
# [BOJ] 19638 센티와 마법의 뿅망치 / 구현, 자료 구조, 우선순위 큐
n, centi_h, t = map(int, input().split())
giant_h = list(-int(input()) for _ in range(n))

heapify(giant_h)
cnt = 0
for i in range(t):
    if -giant_h[0] == 1 or -giant_h[0] < centi_h:
        break
    else:
        heapreplace(giant_h, -(-giant_h[0]//2))
        cnt += 1

if -giant_h[0] >= centi_h:
    print("NO", -giant_h[0], sep='\n')
else:
    print("YES", cnt, sep='\n')