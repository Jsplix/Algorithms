import sys
input = sys.stdin.readline
# [BOJ] 31306 Is Y a Vowel? / 구현, 문자열
s = input().rstrip()
vowel_count = 0
for v in ['a', 'e', 'i', 'o', 'u']:
    vowel_count += s.count(v)
print(vowel_count, vowel_count + s.count('y'))