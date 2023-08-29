import sys
input = sys.stdin.readline
# [BOJ] 1940 주몽 / 정렬, 투 포인터
n = int(input())
m = int(input())
id_num = sorted(list(map(int, input().split())))

lp, rp = 0, n-1
cnt = 0
while lp < rp:
    if id_num[lp] + id_num[rp] == m: cnt += 1; lp += 1; rp -= 1
    elif id_num[lp] + id_num[rp] > m: rp -= 1
    else: lp += 1
print(cnt)