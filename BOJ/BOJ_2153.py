import sys
input = sys.stdin.readline
# [BOJ] 2153 소수 단어 / 수학, 문자열, 정수론, 소수 판정
char_num = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z')+1)}
for i in range(ord('A'), ord('Z')+1):
    char_num[chr(i)] = i - ord('A') + 27

word = input().rstrip()
num = 0
for c in word:
    num += char_num[c]

# 글자 최대 20자, 'Z'는 52 --> 20 * 52 = 1040
prime = [i for i in range(1045)]
prime[0] = 0 # 문제에서 편의상 1도 소수라고 함.
for i in range(2, 1045):
    if not prime[i]: continue
    for j in range(i*i, 1045, i):
        prime[j] = 0

if prime[num]: print("It is a prime word.")
else: print("It is not a prime word.")