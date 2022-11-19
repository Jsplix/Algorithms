# [BOJ] 10987 - 모음의 개수 / 문자열, 구현
s = input()
vowel = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for c in s:
    if c in vowel:
        cnt += 1
print(cnt)