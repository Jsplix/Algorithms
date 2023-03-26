import sys
input = sys.stdin.readline
# [BOJ] 14248 점프 점프 / 그래프 이론, 그래프 탐색, DFS, BFS
n = int(input())
stone = [0] + list(map(int, input().split()))
s = int(input())

bridge = [0 for _ in range(n+1)]
bridge[s] = 1
def move(idx):
    global n
    if 1 <= idx-stone[idx] <= n and not bridge[idx-stone[idx]]:
        bridge[idx-stone[idx]] = bridge[idx] + 1
        move(idx-stone[idx])
    if 1 <= idx+stone[idx] <= n and not bridge[idx+stone[idx]]:
        bridge[idx+stone[idx]] = bridge[idx] + 1
        move(idx+stone[idx])
move(s)
print(n-bridge[1:].count(0))