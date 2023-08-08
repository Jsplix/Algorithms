import sys
input = sys.stdin.readline
# [BOJ] 28431 양말 짝 맞추기 / 구현
socks = { i:0 for i in range(10) }
for _ in range(5):
    socks[int(input())] += 1

for k, v in socks.items():
    if v % 2 == 1: print(k)