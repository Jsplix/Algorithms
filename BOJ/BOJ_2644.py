import sys
input = sys.stdin.readline
# [BOJ] 2644 촌수계산 / 그래프 이론, 그래프 탐색, DFS, BFS
def dfs(k, relations: list):
    global a, b, answer
    if k == b:
        answer = len(relations)
        print(answer)
        exit(0)
    
    for p in geno[k]:
        if not checked[p]:
            checked[p] = 1
            relations.append(p)
            dfs(p, relations)
            relations.pop()
            checked[p] = 0
    
    answer = -1
    return 

n = int(input())
a, b = map(int, input().split())
m = int(input())
geno = [[] for _ in range(n+1)]
checked = [0 for _ in range(n+1)]

answer = 0
for _ in range(m):
    x, y = map(int, input().split())
    geno[x].append(y)
    geno[y].append(x)

dfs(a, [])
print(answer)