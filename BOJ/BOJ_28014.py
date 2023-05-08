import sys
input = sys.stdin.readline
# [BOJ] 28014 첨탑 밀어서 부수기 / 그리디
n = int(input())
h_list = list(map(int, input().split()))

cnt = 1
for i in range(n-1):
    if h_list[i] <= h_list[i+1]: cnt += 1
print(cnt)