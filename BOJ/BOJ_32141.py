import sys
input = sys.stdin.readline
# [BOJ] 32141 카드 게임 (Easy) / 그리디
n, h = map(int, input().split())
cards = list(map(int, input().split()))

if sum(cards) < h: print(-1)
else: 
    count = 0
    for c in cards:
        h -= c
        count += 1
        if h <= 0: break
    
    print(count)