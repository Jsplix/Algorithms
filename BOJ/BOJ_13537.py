import sys
import math
input = sys.stdin.readline
# [BOJ] 13537 수열과 쿼리 1 / 자료 구조, 정렬, 세그먼트 트리, 머지 소트 트리
def initTree(node, start, end):
    if start == end:
        tree[node] = [arr[start]]
        return tree[node]

    mid = (start + end) // 2

    tree[node] = sorted(initTree(node << 1, start, mid) + initTree((node << 1) + 1, mid + 1, end))
    return tree[node]


def query(node, start, end, left, right):
    if (start > right or end < left): return 0
    if (left <= start and right >= end):
        return binarySearch(tree[node])

    mid = (start + end) // 2
    return query(node << 1, start, mid, left, right) + query((node << 1) + 1, mid + 1, end, left, right)

def binarySearch(lst):
    global k
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2

        if lst[mid] > k: right = mid
        else: left = mid + 1

    return len(lst) - left

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

size = 2**math.ceil(math.log2(N))
tree = [[] for _ in range(2 * size + 1)]

for i in range(N):
    tree[size + i] = [arr[i]]

initTree(1, 0, N - 1)

for _ in range(M):
    i, j, k = map(int, input().split())

    print(query(1, 0, N - 1, i - 1, j - 1))