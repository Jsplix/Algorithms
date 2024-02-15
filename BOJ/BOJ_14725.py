import sys
input = sys.stdin.readline
# [BOJ] 14725 개미굴 / 자료 구조, 문자열, 트리, 트라이
class Node():
    def __init__(self, key):
        self.key = key
        self.child = dict()
    
class Trie():
    def __init__(self):
        self.head = Node(None)
    
    def addNode(self, childNode):
        curr = self.head
        for child in childNode:
            if child not in curr.child:
                curr.child[child] = Node(child)
            curr = curr.child[child]

    def printTrie(self, L, curr):
        if L == 0: curr = self.head
        for child in sorted(curr.child.keys()):
            print("--" * L, child, sep="")
            self.printTrie(L + 1, curr.child[child])

n = int(input())
trie = Trie()
for _ in range(n):
    record = list(input().split())
    trie.addNode(record[1:])
trie.printTrie(0, None)