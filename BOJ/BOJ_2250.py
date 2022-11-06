import sys
input = sys.stdin.readline
# BOJ_2250_트리의 높이와 너비
def in_order(node):
    global order
    if node:
        in_order(tree[node][0])
        tree[node][4] = order
        order += 1
        in_order(tree[node][1])

def dfs(now, depth):
    global max_depth
    visited[now] = True
    tree[now][3] = depth
    if max_depth < depth:
        max_depth = depth
    
    for i in range(2):
        if not visited[tree[now][i]]:
            dfs(tree[now][i], depth + 1)

n = int(input())
tree = [ [0, 0, 0, 0, 0] for i in range(n + 1) ]
# 0 = left, 1 = right, 2 = parent, 3 = depth, 4 = width
for _ in range(n):
    node, left, right = map(int, input().split())
    if left == -1:
        left = 0
    if right == -1:
        right = 0
    
    tree[node][0] = left
    tree[node][1] = right

    tree[left][2] = node
    tree[right][2] = node

visited = [False] * (n + 1)
visited[0] = True

root = 0
for i in range(1, n + 1):
    if tree[i][2] == 0:
        root = i
        break

max_depth = 0
dfs(root, 1)
order = 1
in_order(root)

depth_list = [ [] for _ in range(max_depth + 1) ]
for i in range(1, n + 1):
    depth_list[tree[i][3]].append(tree[i][4])

res = []
for i in range(len(depth_list)):
    if len(depth_list[i]) <= 1:
        res.append(1)
    else:
        res.append(max(depth_list[i]) - min(depth_list[i]) + 1)

print(res.index(max(res), 1), max(res))