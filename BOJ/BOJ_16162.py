import sys
input = sys.stdin.readline
# [BOJ] 16162 가희와 3단 고음 / 그리디
n, a, d = map(int, input().split())
arr = list(map(int, input().split()))

target = a
cnt = 0
for x in arr:
    if x == target: 
        cnt += 1
        target += d

print(cnt)