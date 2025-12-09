import sys
from itertools import combinations
input = sys.stdin.readline
# [BOJ] 15686 치킨 배달 / 구현, 브루트포스, 백트래킹, 조합
def get_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken, house = [], []
for row in range(N):
    for col in range(N):
        if city[row][col] == 2:
            chicken.append((row, col))
        elif city[row][col] == 1:
            house.append((row, col))

check = [[] for _ in range(len(chicken))]
sm = []
for i in range(len(chicken)):
    for j in range(len(house)):
        check[i].append(get_distance(chicken[i][0], chicken[i][1], house[j][0], house[j][1]))
    # print(check[i])

# print(check) # i번 치킨집에서 j번 집까지의 거리
result = []
for comb in combinations(range(len(chicken)), M):
    temp = 0
    for i in range(len(house)):
        mn = 101
        for c in comb:
            mn = min(mn, check[c][i])
        temp += mn
    result.append(temp)

print(min(result))