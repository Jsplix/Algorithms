import sys
input = sys.stdin.readline
# [BOJ] 8979 올림픽 / 구현, 정렬
n, k = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]
countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

ranks = {0: 0}
# 이전 국가들의 메달 기록
ranks[countries[0][0]] = 1
pg, ps, pb = countries[0][1:]
for i in range(1, n):
    tg, ts, tb = countries[i][1:]
    if pg > tg:
        ranks[countries[i][0]] = i + 1
    else:
        if ps > ts:
            ranks[countries[i][0]] = i + 1
        else:
            if pb > tb:
                ranks[countries[i][0]] = i + 1
            else:
                ranks[countries[i][0]] = ranks[countries[i-1][0]]
    
    pg, ps, pb = tg, ts, tb

print(ranks[k])