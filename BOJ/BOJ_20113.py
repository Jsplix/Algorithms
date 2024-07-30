import sys
from collections import defaultdict
input = sys.stdin.readline
# [BOJ] 20113 긴급 회의 / 구현
d = defaultdict(int)
n = int(input())
arr = list(map(int, input().split()))

for a in arr:
    if a == 0: continue
    d[a] += 1

lst = list(d.items())
lst.sort(key=lambda x: -x[1])

mx = lst[0][1]
count = 0
for k, v in lst:
    if v == mx: 
        count += 1

if count >= 2: print("skipped")
else: print(lst[0][0])