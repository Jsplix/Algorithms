import sys
input = sys.stdin.readline
# [BOJ] 2845 파티가 끝나고 난 뒤 / 수학, 구현
a, b = map(int, input().split())
l = list(map(int, input().split()))

for i in range(len(l)):
    print(l[i] - (a * b), end = ' ')