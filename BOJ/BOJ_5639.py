import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
# [BOJ] 5639 이진 검색 트리 / 그래프 이론, 그래프 탐색, 트리, 재귀
nodes = []
while True:
    try:
        v = int(input())
        nodes.append(v)
    except:
        break


def traversal(arr: list):
    
    if len(arr) == 0: return

    root = arr[0]
    left, right = [], []

    for i in range(1, len(arr)):
        if arr[i] < root: left.append(arr[i])
        else: right.append(arr[i])

    traversal(left)
    traversal(right)
    print(root)

traversal(nodes)