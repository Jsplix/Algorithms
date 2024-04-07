import sys
input = sys.stdin.readline
# [BOJ] 14645 와이버스 부릉부릉 / 구현
n, k = map(int, input().split())
st = [list(map(int, input().split())) for _ in range(n)]
print("비와이")