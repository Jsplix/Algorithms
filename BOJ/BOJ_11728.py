import sys
input = sys.stdin.readline
# [BOJ] 11728 배열 합치기 / 정렬, 투 포인터
n, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
print(*list(sorted(arr_a+arr_b)))