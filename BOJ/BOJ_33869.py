import sys
input = sys.stdin.readline
# [BOJ] 33869 일기 암호화하기 / 구현, 문자열
W = input().rstrip()
S = input().rstrip()

secret = {}

word = ''
for c in W:
    if c not in word:
        word += c

for i in range(len(word)):
    secret[chr(ord('A') + i)] = word[i]

a = 0
for i in range(26 - len(word)):
    now = chr(ord('A') + a)
    while now in word: 
        a += 1
        now = chr(ord('A') + a)

    secret[chr(ord('A') + len(word) + i)] = now
    a += 1

result = ''
for c in S:
    result += secret[c]
print(result)