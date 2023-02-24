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

# house[(n-1)//2]로 간단히 구할 수 있음.
# 특정 집의 위치를 기준으로 왼쪽 집의 개수가 오른쪽 집의 개수보다 많아지면 안됨.
# 왼쪽 집의 개수가 오른쪽 집의 개수를 넘어서기 직전이 모든 집까지의 거리가 최소가 되는 집.
# 그 이유는 가장 왼쪽 집으로부터 각 집들까지의 거리를 구하면 오른쪽으로 갈수록 거리가 줄어들다가 왼쪽 집의 개수가 더 많아지는 순간
# 다시 거리가 증가하게 되기 때문임.