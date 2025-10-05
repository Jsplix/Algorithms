import sys
input = sys.stdin.readline
# [BOJ] 3059 등장하지 않는 문자의 합 / 구현, 문자열
for _ in range(int(input())):
    s = set(input().rstrip())
    total = 0
    for i in range(ord('A'), ord('Z') + 1):
        total += i

    for c in s:
        total -= ord(c)
    print(total)