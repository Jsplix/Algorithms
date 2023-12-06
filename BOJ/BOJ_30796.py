import sys
input = sys.stdin.readline
# [BOJ] 30796 gahui and sousenkyo 4 / 그리디, 해 구성하기
v, k = map(int, input().split())
left, right = 1, v

ranked = {i:1 for i in range(v, -1, -1)}
p, cnt = [], 0
gap = -1 if k != 1 else -2
for i in range(v, 0, gap):
    if i - k <= 0: break
    if not ranked[i]: continue
    ranked[i-k] -= 1

for j in range(v, 0, -1):
    if ranked[j]: 
        p.append(j); cnt += 1
print(cnt, *p, sep='\n')