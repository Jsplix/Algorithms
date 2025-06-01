import sys
input = sys.stdin.readline
# [BOJ] 33950 어게인 포닉스 / 구현, 문자열
for _ in range(int(input())):
    s = input().rstrip()
    print(s.replace('PO', 'PHO'))