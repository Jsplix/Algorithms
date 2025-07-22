import sys
input = sys.stdin.readline
# [BOJ] 10769 행복한지 슬픈지 / 구현, 문자열, 파싱
s = input().rstrip()
a, b = 0, 0
a += s.count(':-)')
b += s.count(':-(')

if not a and not b: print("none")
elif a == b: print("unsure")
elif a < b: print("sad")
else: print("happy")