import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
# [BOJ] 24230 트리 색칠하기 / 그래프 이론, 그래프 탐색, 트리, DFS
def DFS(node, color, sequence: set):
    global count
    for next_node in trees[node]:
        if next_node not in sequence:
            sequence.add(next_node)
            if color != c[next_node]:
                count += 1
            temp[next_node] = c[next_node]
            DFS(next_node, c[next_node], sequence)
    
n = int(input())
c = [0] + list(map(int, input().split()))
trees = [[] for _ in range(n+1)]
temp = [0 for _ in range(n+1)] # current node color - all white
for _ in range(n-1):
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

count = 0 if not c[1] else 1
DFS(1, c[1], set([1]))

print(count)