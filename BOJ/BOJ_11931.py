import sys
input = sys.stdin.readline
# [BOJ] 11931 수 정렬하기 4 / 정렬
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
print(*arr, sep='\n')