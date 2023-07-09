import sys
input = sys.stdin.readline
# [BOJ] 11971 속도 위반 / 구현
n, m = map(int, input().split())
limit = [0 for _ in range(101)]
cur = [0 for _ in range(101)]
diff = [0 for _ in range(101)]
l = 0

for _ in range(n):
    r, s = map(int, input().split())
    for i in range(l+1, l+r+1):
        limit[i] = s
    l += r

l, r = 0, 0
for _ in range(m):
    r, s = map(int, input().split())
    for i in range(l+1, l+r+1):
        cur[i] = s
    l += r

for k in range(1, 101):
    diff[k] = cur[k] - limit[k]
answer = max(diff)

if answer <= 0: print(0)
else: print(answer)