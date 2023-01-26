import sys
input = sys.stdin.readline
# [BOJ] 2246 콘도 선정 / 브루트 포스, 정렬
n = int(input())
condo = [list(map(int, input().split())) for _ in range(n)]
answer = 0
# pypy3으로 제출해야 통과
for i in range(n):
    chk = 0
    std_dist = condo[i][0]
    std_price = condo[i][1]
    for j in range(n):
        if i == j: continue
        if condo[j][0] < std_dist and condo[j][1] < std_price:
            break
        if condo[j][0] < std_dist and condo[j][1] > std_price:
            chk += 1
        if condo[j][0] > std_dist and condo[j][1] < std_price:
            chk += 1
        if condo[j][0] >= std_dist and condo[j][1] >= std_price:
            chk += 1
    if chk == n-1: answer += 1

print(answer)