import sys
input = sys.stdin.readline
# [BOJ] 13277 큰 수 곱셈 / 수학, 사칙연산
# 큰 수를 지원하지 않는 C++의 경우는 문자열 처리로 구현하면 될 듯함.
a, b = map(int, input().split())
print(a * b)