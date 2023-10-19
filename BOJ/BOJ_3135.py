import sys
input = sys.stdin.readline
# [BOJ] 3135 라디오 / 수학, 그리디
now, after = map(int, input().split())
n = int(input())
freq = sorted(int(input()) for _ in range(n))

for i in range(n):
    freq[i] = abs(freq[i] - after) + 1

print(min(abs(now-after), min(freq)))