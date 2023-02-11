import sys
input = sys.stdin.readline
# [BOJ] 13305 주유소 / 그리디
n = int(input())
city_gap = list(map(int, input().split()))
oil = list(map(int, input().split()))

now_cost = oil[0] * city_gap[0]
last = oil[0]
for i in range(1, n-1):
    if last < oil[i]:
        now_cost += last * city_gap[i]
    else:
        last = oil[i]
        now_cost += last * city_gap[i]

print(now_cost)