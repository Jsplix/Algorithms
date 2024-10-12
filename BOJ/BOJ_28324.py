import sys
input = sys.stdin.readline
# [BOJ] 28324 스케이트 연습 / 그리디
n = int(input())
v = list(map(int, input().split()))

vn, total = 0, 0
for vs in v[::-1]:
    if vn < vs:
        vn += 1
    else:
        vn = vs

    total += vn

print(total)