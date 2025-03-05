import sys
input = sys.stdin.readline
# [BOJ] 29615 알파빌과 베타빌 / 그리디
n, m = map(int, input().split())
waiting = list(map(int, input().split()))
friends = list(map(int, input().split()))

count = 0
for i in range(m, n):
    if waiting[i] in friends:
        count += 1
print(count)