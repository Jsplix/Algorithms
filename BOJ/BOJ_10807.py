import sys
input = sys.stdin.readline
# [BOJ] 10807 개수 세기 / 구현
n = int(input())
arr = list(map(int, input().split()))
s_num = int(input())

print(arr.count(s_num))