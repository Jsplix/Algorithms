from itertools import permutations
import sys
input = sys.stdin.readline
# [BOJ] 16943 숫자 재배치 / 수학, 브루트 포스, 조합론, 백트래킹
a, b = input().split()
a_list = list(map(int, a))
b_list = list(map(int, b))

c_list = list(permutations(a_list))
possible = []
for p in c_list:
    if p[0] == 0: continue
    val = int(''.join(map(str, p)))
    if val < int(b):
        possible.append(val)

if len(possible) == 0: print(-1)
else: print(max(possible))