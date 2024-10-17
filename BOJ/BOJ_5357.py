import sys
input = sys.stdin.readline
# [BOJ] 5357 Dedupe / 구현, 문자열
for _ in range(int(input())):
    answer = ''
    s = input().rstrip()
    answer += s[0]
    for i in range(1, len(s)):
        if answer[-1] != s[i]:
            answer += s[i]
    print(answer)