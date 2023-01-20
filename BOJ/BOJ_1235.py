import sys
input = sys.stdin.readline
# [BOJ] 1235 학생 번호 / 구현, 문자열
n = int(input())
st_id = [input().rstrip() for _ in range(n)]
k = 1
id_len = len(st_id[0])
res = 0

while not res:
    chk = {}
    for i in range(n):
        if st_id[i][id_len-k:] not in chk:
            chk[st_id[i][id_len-k:]] = 1
        else: chk[st_id[i][id_len-k:]] += 1
    v = list(chk.values())
    if v.count(1) == n: res = k
    else: k += 1

print(k)