import sys
from itertools import combinations
input = sys.stdin.readline
# [BOJ] 1450 냅색문제 / 이분 탐색, 중간에서 만나기(MITM: Meet In The Middle)
n, c = map(int, input().split())
items = list(map(int, input().split()))

left = items[:n // 2]
right = items[n // 2:]

left_sum, right_sum = [], []
for i in range(len(left) + 1):
    for comb in combinations(left, i):
        left_sum.append(sum(comb))

for i in range(len(right) + 1):
    for comb in combinations(right, i):
        right_sum.append(sum(comb))

left_sum.sort()
right_sum.sort()
result = 0

s = 0
e = len(right_sum) - 1

while s != len(left_sum) and e >= 0:
    if left_sum[s] + right_sum[e] <= c:
        result += (e + 1)
        s += 1
    else:
        e -= 1

print(result)