import sys
input = sys.stdin.readline
# [BOJ] 27111 출입 기록 / 구현, 애드혹
records = [0 for _ in range(200001)]
loss = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if records[a] == b:
        loss += 1
    else:
        records[a] = b
loss += records.count(1)
print(loss)