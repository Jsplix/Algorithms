import sys
input = sys.stdin.readline
# [BOJ] 16562 친구비 / 자료 구조, 그래프 이론, 그래프 탐색, 분리 집합
n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
vertex = [i for i in range(n+1)]

def union(v, w):
    pv, pw = find(v), find(w)
    if cost[pv] < cost[pw]: 
        vertex[pw] = pv
    else: 
        vertex[pv] = pw

def find(x):
    if vertex[x] != x: 
        vertex[x] = find(vertex[x])
    return vertex[x]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n+1):
    vertex[i] = find(i)

total = 0
for x in set(vertex[1:]):
    if x == 0: continue
    total += cost[x]

if total <= k: print(total)
else: print("Oh no")