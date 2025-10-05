import sys
input = sys.stdin.readline
# [BOJ] 20040 사이클 게임 / 자료 구조, 분리 집합
def find(x):
    if parents[x] != x: 
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if (px == py): return True
    elif (px < py): parents[py] = px
    else: parents[px] = py
    return False

n, m = map(int, input().split())

parents = [i for i in range(n)]
flag = False
answer = 0
for cnt in range(1, m+1):
    a, b = map(int, input().split())

    if flag: continue

    if (union(a, b)):
        answer = cnt
        flag = True
        continue

print(answer)