import sys
input = sys.stdin.readline
# [BOJ] 16212 정열적인 정렬 / 정렬
n=int(input()); print(*sorted(list(map(int, input().split()))), end=' ')