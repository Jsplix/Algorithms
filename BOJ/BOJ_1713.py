import sys
input = sys.stdin.readline
# [BOJ] 1713 후보 추천하기 / 구현, 시뮬레이션
n = int(input())
recomm_cnt = int(input())
st_id = list(map(int, input().split()))

d = {}; upload = 0
for i in range(recomm_cnt):
    if st_id[i] not in d.keys():
        if upload == n:
            d_li = sorted(list(d.items()), key=lambda x:(x[1][0], x[1][1]))
            del d[d_li[0][0]]
            upload -= 1
        d[st_id[i]] = [1, i]
        upload += 1
    else:
        d[st_id[i]][0] += 1

print(*sorted(list(d.keys())))