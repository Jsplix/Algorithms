import sys
input = sys.stdin.readline
# [BOJ] 29713 브실이의 띠부띠부씰 컬렉션 🍪 / 구현, 문자열
d = {'B': 0, 'R': 0, 'O': 0, 'N': 0, 'Z': 0, 'E': 0, 'S': 0, 'I': 0, 'L': 0, 'V': 0}
# R - 2, E - 2
n = int(input())
s = input().rstrip()
for c in s:
    if c not in d.keys(): continue
    d[c] += 1

cnt = 0
while min(d.values()) > 0:
    flag = False
    for k in 'BRONZESILVER':
        if d[k] <= 0: flag = True
        d[k] -= 1
    if not flag: cnt += 1
    else: break
print(cnt)