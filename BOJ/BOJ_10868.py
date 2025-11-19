import sys
input = sys.stdin.readline
# [BOJ] 10868 최솟값 / 자료 구조, 세그먼트 트리, 희소 배열
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

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

tree = [0 for _ in range(4 * N + 1)]

initTree(1, 0, N - 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(query(1, 0, N - 1, a - 1, b - 1))