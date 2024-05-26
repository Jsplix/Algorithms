import sys
input = sys.stdin.readline
# [BOJ] 31880 K512컵 개최! / 수학, 그리디, 사칙연산
n, m = map(int, input().split())
f = list(map(int, input().split()))
s = sorted(list(map(int, input().split())))
p = 0

f_sum = sum(f)
last_zero = -1
for i in range(m):
    if s[i] == 0: last_zero = i
    else: break

if last_zero == -1:
    p = f_sum
    for x in s:
        p *= x
else:
    p = f_sum
    for x in s[last_zero+1:]:
        p *= x

print(p)