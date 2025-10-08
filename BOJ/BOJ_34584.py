import sys
input = sys.stdin.readline
# [BOJ] 34584 Take It or Double It / 수학, 사칙연산
a, b = map(int, input().split())
print("double it" if a * 2 <= b else "take it")