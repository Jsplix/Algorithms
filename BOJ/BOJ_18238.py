import sys
input = sys.stdin.readline
# [BOJ] 18238 ZOAC 2 / 구현, 그리디, 문자열
prev = 'A'
word = input().rstrip()

result = 0
for c in word:
    if ord(c) <= ord(prev):
        left = ord(prev) - ord(c)
        right = ord('Z') - ord(prev) + ord(c) - ord('A') + 1
    else:
        left = ord(prev) - ord('A') + ord('Z') - ord(c) + 1
        right = ord(c) - ord(prev)

    result += min(left, right)
    prev = c
print(result)