import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 18115 카드 놓기 / 자료 구조, 덱
n = int(input())
skill_list = list(map(int, input().split()))[::-1]
cards = deque([]) 

for i in range(n):
    if skill_list[i] == 1:
        cards.append(i+1)
    elif skill_list[i] == 2:
        cards.insert(-1, i+1)
    elif skill_list[i] == 3:
        cards.appendleft(i+1)

print(*reversed(cards))