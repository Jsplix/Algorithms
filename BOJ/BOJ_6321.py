import sys
input = sys.stdin.readline
# [BOJ] 6321 IBM 빼기 1 / 구현, 문자열
for tc in range(1, int(input())+1):
    s = input().rstrip()
    result = ''
    for c in s:
        result += chr((ord(c) - ord('A') + 1) % 26 + ord('A'))
    print("String #%d" % tc, result, sep='\n')
    print("")