import sys
input = sys.stdin.readline
# [BOJ] 14427 수열과 쿼리 15 / 자료 구조, 세그먼트 트리, 우선순위 큐
def init(node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]

    mid = (start + end) // 2
    l = init((node << 1), start, mid)
    r = init((node << 1) + 1, mid + 1, end)

    tree[node] = l if arr[l] <= arr[r] else r
    return tree[node]

def update(node, start, end, index, value):
    if start > index or end < index: 
        return

    if start == end:
        tree[node] = index
        return

    mid = (start + end) // 2
    update((node << 1), start, mid, index, value)
    update((node << 1) + 1, mid + 1, end, index, value)

    tree[node] = tree[(node << 1)] if arr[tree[(node << 1)]] <= arr[tree[(node << 1) + 1]] else tree[(node << 1) + 1]
    return 

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

tree = [0 for _ in range(4 * N + 1)]
init(1, 0, N - 1)

for _ in range(M):
    comm = list(map(int, input().split()))
    if comm[0] == 1:
        arr[comm[1] - 1] = comm[2]
        update(1, 0, N - 1, comm[1] - 1, comm[2])
    else:
        print(tree[1] + 1)