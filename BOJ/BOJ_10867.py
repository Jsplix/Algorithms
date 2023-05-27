import sys
input = sys.stdin.readline
# [BOJ] 10867 중복 빼고 정렬하기 / 정렬
n = int(input())
arr = list(set(map(int, input().split())))
arr.sort()
print(*arr)