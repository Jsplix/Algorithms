import sys
input = sys.stdin.readline
# [BOJ] 18310 안테나 / 수학, 그리디, 정렬
n = int(input())
house = sorted(list(map(int, input().split())))

idx = house.index(house[n//2])
dist = 0
for i in range(n):
    dist += abs(house[idx]-house[i])
mn = dist

for i in range(idx-1, min(idx+2, n)):
    chk_dist = 0
    if i == idx: continue
    for j in range(n):
        chk_dist += abs(house[i]-house[j])
    if mn > chk_dist: idx = i
    elif mn == chk_dist: idx = i if i <= idx else idx
    else: continue

print(house[idx])