import sys
input = sys.stdin.readline
# [BOJ] 13985 Equality / 수학, 문자열, 사칙연산
arithmetic = input().split()
a, b, c = map(int, [arithmetic[0], arithmetic[2], arithmetic[4]])
print("YES" if a+b==c else "NO")