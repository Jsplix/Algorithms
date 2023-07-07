import sys
input = sys.stdin.readline
# [BOJ] 14391 종이 조각 / 브루트 포스, 비트마스킹
# bitmask problem / 0 - 세로, 1 - 가로
def bitmasking():
    global max_value
    for i in range(1 << n * m):
        total = 0
        for row in range(n):
            rowsum = 0
            for col in range(m):
                idx = row * m + col
                if i & ( 1 << idx ) != 0:
                    rowsum = rowsum * 10 + paper[row][col]
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum

        for col in range(m):
            colsum = 0
            for row in range(n):
                idx = row * m + col
                if i & ( 1 << idx ) == 0:
                    colsum = colsum * 10 + paper[row][col]
                else:
                    total += colsum
                    colsum = 0
            total += colsum
        max_value = max(total, max_value)

n, m = map(int, input().split())
paper = [ list(map(int, input().rstrip())) for _ in range(n) ]
max_value = 0

bitmasking()
print(max_value)