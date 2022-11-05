import sys
input = sys.stdin.readline

n = int(input())
board = [ [0 for _ in range(100)] for _ in range(100) ]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            board[x - 1 + i][y - 1 + j] += 1
area = 100**2
for i in range(100):
    area -= board[i].count(0)
print(area)