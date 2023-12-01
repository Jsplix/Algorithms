import sys
input = sys.stdin.readline
# [BOJ] 1669 멍멍이 쓰다듬기 / 수학
x, y = map(int, input().split())
gap = y-x

if not gap: print(0)
else:
    n = 0
    while n**2 < gap:
        n += 1
    if n * n != gap: n -= 1
    answer = 2*n-1
    gap -= n**2

    while gap > 0:
        gap -= min(n, gap)
        answer += 1
    print(answer)