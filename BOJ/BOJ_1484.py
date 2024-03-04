import sys
input = sys.stdin.readline
# [BOJ] 1484 다이어트 / 수학, 투 포인터
g = int(input())
chk = [0] + [i**2 for i in range(1, 50002)]

l, r = 1, 2 # r - 현재, l - 과거
flag = False
while l <= r and r <= 50001:
    res = chk[r] - chk[l]
    if res == g:
        print(r)
        l += 1
        r += 1
        flag = True
    else:
        if res < g: r += 1
        else: l += 1

if not flag: print(-1) # 가능한 몸무게가 없는 경우.