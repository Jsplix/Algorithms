from math import sqrt
import sys
input = sys.stdin.readline
# [BOJ] 1977 완전제곱수 / 브루트 포스
n = int(input())
m = int(input())

chk = []
for i in range(n, m + 1):
    if i == (int(sqrt(i)))**2:
        chk.append(i)

if chk != []:
    print(str(sum(chk)) + '\n' + str(min(chk)))
else:
    print(-1)