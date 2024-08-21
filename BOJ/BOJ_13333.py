import sys
input = sys.stdin.readline
# [BOJ] 13333 Q-인덱스 / 브루트포스, 정렬
n = int(input())
docs = sorted(map(int, input().split()))

for i in range(n, -1, -1):
    if i <= docs[-i]:
        print(i)
        break