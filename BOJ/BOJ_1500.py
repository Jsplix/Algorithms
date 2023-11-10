import sys
input = sys.stdin.readline
# [BOJ] 1500 최대 곱 / 수학
s, k = map(int, input().split())
q, r = s//k, s%k

ans = 1
for i in range(k):
    if r > 0: ans *= (q+1); r -= 1
    else: ans *= q
print(ans)