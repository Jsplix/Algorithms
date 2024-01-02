import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
# [BOJ] 16432 떡장수와 호랑이 / DP, 그래프 이론, 그래프 탐색, DFS
n = int(input())
sell = []
for _ in range(n):
    m, *tteok = map(int, input().split())
    sell.append(tteok)
checking = [[0 for i in range(10)] for _ in range(n+1)]

def dfs(day, give):

    if day == n:
        print(*give[1:], sep='\n')
        exit()
    
    for g in sell[day]:
        if g != give[-1] and not checking[day][g]:
            checking[day][g] = 1
            dfs(day + 1, give + [g])

dfs(0, [0])
print(-1)