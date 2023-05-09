import sys
input = sys.stdin.readline
# [BOJ] 1246 온라인 판매 / 정렬, 그리디
n, m = map(int, input().split())
prices = [int(input()) for _ in range(m)]
prices.sort()

total = -1
p = -1
for i in range(m):
    e = min(m-i, n)

    if total < prices[i] * e:
        p = prices[i]
        total = prices[i] * e

print(p, total)