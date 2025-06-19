import sys
input = sys.stdin.readline
# [BOJ] 15819 너의 핸들은 / 문자열, 정렬
n, k = map(int, input().split())
handles = sorted(input().rstrip() for _ in range(n))
print(handles[k-1]) 