import sys
input = sys.stdin.readline
# [BOJ] 14428 수열과 쿼리 16 / 자료 구조, 세그먼트 트리
LIM = 10**9 + 9

def init(node, start, end):
    if start == end:
        tree[node][0] = arr[start]
        tree[node][1] = start + 1
        return tree[node]
    
    mid = (start + end) // 2
    tree[node] = min(init(node << 1, start, mid), init((node << 1) + 1, mid + 1, end))
    return tree[node]

def query(node, start, end, left, right):
    if start > right or end < left: return [LIM, LIM]
    
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return min(query(node << 1, start, mid, left, right), query((node << 1) + 1, mid + 1, end, left, right))

def update(node, start, end, index, value):
    if index < start or index > end:
        return [LIM, LIM]
    
    if start == end:
        tree[node][0] = value
        return
    
    mid = (start + end) // 2
    update(node << 1, start, mid, index, value)
    update((node << 1) + 1, mid + 1, end, index, value)
    
    tree[node] = min(tree[node << 1], tree[(node << 1) + 1])

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

tree = [[LIM, -1] for _ in range(4 * N)]

init(1, 0, N - 1)
for _ in range(M):
    k, *q = map(int, input().split())
    if k == 1:
        arr[q[0] - 1] = q[1]
        update(1, 0, N - 1, q[0] - 1, q[1])
    else:
        print(query(1, 0, N - 1, q[0] - 1, q[1] - 1)[1])