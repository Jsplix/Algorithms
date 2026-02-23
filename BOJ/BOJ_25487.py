import sys
input = sys.stdin.readline
# [BOJ] 25487 단순한 문제 (Large) / 수학, 정수론
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(min(a, b, c))