import sys
from collections import defaultdict
input = sys.stdin.readline
# [BOJ] 21921 블로그 / 누적 합, 슬라이딩 윈도우
n, x = map(int, input().split())
visitors = list(map(int, input().split()))

count = defaultdict(int)
views = sum(visitors[:x])
count[views] = 1
mx = views
for i in range(x, n):
    temp = views - visitors[i-x] + visitors[i]
    count[temp] += 1
    if mx < temp: 
        mx = temp
    views = temp
    
if not mx: print("SAD")
else: print(mx, count[mx], sep='\n')