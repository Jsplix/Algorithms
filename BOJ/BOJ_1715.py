from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 1715 카드 정렬하기 / 자료 구조, 그리디, 우선순위 큐
n = int(input())
cards = [int(input()) for _ in range(n)]
cards.sort()
# 핵심은 가능한 한 카드의 수가 작은 묶음끼리 합쳐야 한다는 것임.
cmp_cnt = 0
while len(cards) != 1:
    mn_1 = heappop(cards)
    mn_2 = heappop(cards)
    
    sm = mn_1 + mn_2
    cmp_cnt += sm
    heappush(cards, sm)

print(cmp_cnt)