import sys
input = sys.stdin.readline
# [BOJ] 1251 단어 나누기 / 구현, 문자열, 브루트 포스, 정렬
s = input().rstrip()
chk = []
# h, b, t = '', '', ''
for i in range(1, len(s)):
    for j in range(i + 1, len(s)):
        h, b, t = '', '', ''
        h += s[:i]
        b += s[i:j]
        t += s[j:]

        chk.append(h[::-1] + b[::-1] + t[::-1])
chk.sort()
print(chk[0])