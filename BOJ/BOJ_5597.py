import sys
input = sys.stdin.readline
# [BOJ] 5597 과제 안 내신 분..? / 구현
l = {k : 0 for k in range(1, 31)}
for i in range(28):
    l[int(input())] = 1

for x in range(1, 31):
    if not l[x]:
        print(x)