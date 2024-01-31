import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
# [BOJ] 16437 양 구출 작전 / 그래프 이론, 그래프 탐색, 트리, DFS
n = int(input())
islands = [[0, 0] for _ in range(n+1)] # 0 - 양 / 1 - 늑대
trees = [[] for _ in range(n+1)]

for i in range(2, n+1):
    animalType, cnt, to = input().split()
    cnt = int(cnt)
    to = int(to)
    trees[to].append(i)

    if animalType == 'W': islands[i][1] = cnt
    else: islands[i][0] = cnt

def solve(now):
    ret = 0
    
    for next in trees[now]:
        ret += solve(next)
    
    if not islands[now][0] and islands[now][1]:
        ret -= islands[now][1]
        if ret < 0: ret = 0
    else:
        ret += islands[now][0]
    
    return ret

print(solve(1))