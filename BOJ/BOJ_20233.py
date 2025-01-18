import sys
input = sys.stdin.readline
# [BOJ] 20233 Bicycle / 수학, 사칙연산
info = [int(input()) for _ in range(5)]
f, s = info[0], info[2]
f += 21 * (info[4]-30 if info[4] > 30 else 0) * info[1]
s += 21 * (info[4]-45 if info[4] > 45 else 0) * info[3]

print(f, s)