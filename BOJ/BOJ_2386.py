import sys
input = sys.stdin.readline
# [BOJ] 2386 도비의 영어 공부 / 구현, 문자열, 브루트 포스
while True:
    s = input().rstrip().lower()
    if s == '#': break
    c = s[0]
    s = s[2:]
    print(c, s.count(c))