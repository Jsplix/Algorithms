import sys
input = sys.stdin.readline
# [BOJ] 1414 불우이웃돕기 / 그래프 이론, 문자열, 최소 스패닝 트리
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

d = {'0': 0}
for i in range(26):
    d[chr(ord('a')+i)]=i+1
    d[chr(ord('A')+i)]=i+27

n = int(input())
parents = [i for i in range(n)]
edges = []

result = 0
for i in range(n):
    adjacency = list(input().rstrip())
    for j in range(n):
        if adjacency[j] == '0': edges.append((i, j, 0))
        else:
            result += d[adjacency[j]]
            edges.append((i, j, d[adjacency[j]]))

edges.sort(key=lambda x:x[2])
for s, e, weight in edges:
    if weight == 0: continue
    if find(s) != find(e):
        union(s, e)
        result -= weight

check = set()
for i in range(n):
    tmp = find(i)
    if tmp not in check:
        check.add(tmp)

if len(check) == 1: print(result)
else: print(-1)