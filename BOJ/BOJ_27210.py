import sys
input = sys.stdin.readline
# [BOJ] 27210 신을 모시는 사당 / DP, 누적 합
n = int(input())
sculptures = list(map(int, input().split()))
l, r = 0, 0

answer = 0
for sc in sculptures:
    if sc == 1:
        l += 1
        r -= 1
    else:
        l -= 1
        r += 1
    
    if l < 0: l = 0
    if r < 0: r = 0

    answer = max(l, r, answer)
print(answer)