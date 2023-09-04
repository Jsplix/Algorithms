import sys
input = sys.stdin.readline
# [BOJ] 14467 소가 길을 건너간 이유 1 / 구현
dic, cnt = {}, 0
for _ in range(int(input())):
    c, d = map(int, input().split())
    if c not in dic.keys():
        dic[c] = d
    else:
        if dic[c] == d: continue
        else:
            cnt += 1
            dic[c] = d
print(cnt)