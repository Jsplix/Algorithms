import sys
input = sys.stdin.readline
# [BOJ] 열 개씩 끊어 출력하기 / 구현, 문자열
s = input().rstrip()
c = 0
for _ in range((len(s) // 10) + 1):
    print(s[c: c + 10])
    c += 10