import sys
input = sys.stdin.readline
# [BOJ] 5576 콘테스트 / 구현, 정렬
w = [int(input()) for _ in range(10)]
k = [int(input()) for _ in range(10)]
w.sort(); k.sort()
print(w[-1] + w[-2] + w[-3], k[-1] + k[-2] + k[-3])