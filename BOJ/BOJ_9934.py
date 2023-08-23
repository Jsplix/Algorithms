import sys
input = sys.stdin.readline
# [BOJ] 9934 완전 이진 트리 / 트리, 재귀
k = int(input())
buildings = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def bTree(bd, x):
    mid = len(bd) // 2
    tree[x].append(bd[mid])
    if len(bd) == 1: return
    bTree(bd[:mid], x+1)
    bTree(bd[mid+1:], x+1)

bTree(buildings, 0)
for node in tree:
    print(*node)