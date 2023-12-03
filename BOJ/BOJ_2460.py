import sys
input = sys.stdin.readline
# [BOJ] 2460 지능형 기차 2 / 수학, 구현, 사칙연산
people = 0
mx = 0
for _ in range(10):
    o, i = map(int, input().split())
    people -= o
    people += i
    mx = max(people, mx)
print(mx)