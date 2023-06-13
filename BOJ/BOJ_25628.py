import sys
input = sys.stdin.readline
# [BOJ] 25628 햄버거 만들기 / 수학, 사칙연산
a, b = map(int, input().split())
answer = 0

while a > 1 and b > 0:
    answer += 1
    a -= 2
    b -= 1

print(answer)