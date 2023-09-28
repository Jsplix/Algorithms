import sys
input = sys.stdin.readline
# [BOJ] 25644 최대 상승 / 구현, DP, 그리디
n = int(input())
ana = list(map(int, input().split()))

mx = 0
lp, rp = 0, 1

while rp != n:
    if ana[lp] < ana[rp]:
        mx = max(mx, ana[rp]-ana[lp])
        rp += 1
    else:
        lp += 1
    if lp == rp: rp += 1
print(mx)