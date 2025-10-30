import sys
from collections import defaultdict
input = sys.stdin.readline
# [BOJ] 4195 친구 네트워크 / 자료 구조, 집합과 맵, 해시를 사용한 집합과 맵, 분리 집합(유니온 파인드)
def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)
    
    if px < py:
        parent[py] = px
        relations[px] += relations[py]
        return relations[px]
    elif px > py:
        parent[px] = py 
        relations[py] += relations[px]
        return relations[py]
    else:
        return relations[px]

for _ in range(int(input())):
    F = int(input())
    parent = [i for i in range(2 * F)]
    relations = [1 for _ in range(2 * F)]
    names = defaultdict(lambda: -1)
    
    idx = 0
    for __ in range(F):
        nm1, nm2 = input().split()
        
        if names[nm1] == -1:
            names[nm1] = idx
            idx +=1
        
        if names[nm2] == -1:
            names[nm2] = idx
            idx += 1

        print(union(names[nm1], names[nm2]))