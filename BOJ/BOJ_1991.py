import sys
input = sys.stdin.readline
# [BOJ] 1991 트리 순회 / 트리, 재귀
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
def pre_order(node):
    print(node.data, end = '')
    if node.left != None:
        pre_order(tree[node.left])
    if node.right != None:
        pre_order(tree[node.right])

def in_order(node):
    if node.left != None:
        in_order(tree[node.left])
    print(node.data, end = '')
    if node.right != None:
        in_order(tree[node.right])

def post_order(node):
    if node.left != None:
        post_order(tree[node.left])
    if node.right != None:
        post_order(tree[node.right])
    print(node.data, end = '')

n = int(input())
tree = {}

for _ in range(n):
    d, l, r = input().split()
    if l == '.':
        l = None
    if r == '.':
        r = None
    tree[d] = Node(d, l, r)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])