import sys
input = sys.stdin.readline
# [BOJ] 14438 수열과 쿼리 17 / 자료 구조, 세그먼트 트리
def initTree(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    tree[node] = min(initTree(node << 1, start, mid), initTree((node << 1) + 1, mid + 1, end))
    return tree[node]

def query(node, start, end, left, right):
    if left > end or right < start:
        return 10**9 + 9
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return min((query((node << 1), start, mid, left, right), query((node << 1) + 1, mid + 1, end, left, right)))

def update(node, start, end, index, value):
    if start > index or end < index: return

    if start != end:
        mid = (start + end) // 2
        update((node << 1), start, mid, index, value)
        update((node << 1) + 1, mid + 1, end, index, value)
        tree[node] = min(tree[(node << 1)], tree[(node << 1) + 1])
    else:
        tree[node] = value


N = int(input())
arr = list(map(int, input().split()))
M = int(input())

tree = [0 for _ in range(4 * N + 1)]
initTree(1, 0, N - 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1: 
        update(1, 0, N - 1, b - 1, c)
    else:
        print(query(1, 0, N - 1, b - 1, c - 1))