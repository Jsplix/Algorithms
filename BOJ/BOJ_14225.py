from collections import Counter
from itertools import combinations
import sys
input = sys.stdin.readline
# [BOJ] 14225 부분수열의 합 / 브루트 포스, 백트래킹
# 백트래킹으로도 풀 수 있을듯 함.
n = int(input())
s = list(map(int, input().split()))
u = []

for i in range(len(s) + 1):
    combine = combinations(s, i)
    for subarr in combine:
        u.append(sum(subarr))
u.sort()
chk = [i for i in range(1, u[-1] + 2)] # 마지막수, 마지막수 + 1이 포함되어야 하므로 +2해줌
u = list(set(u[1:]))

result = Counter(chk) - Counter(u)
print(list(result.keys())[0])