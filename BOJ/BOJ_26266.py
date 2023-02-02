import sys
input = sys.stdin.readline
# [BOJ] 26266 비즈네르 암호 해독 / 브루트 포스, 문자열, 수학, 정수론
clear_text = list(input().rstrip())
coded_text = list(input().rstrip())

n = len(clear_text)
k = [0 for _ in range(n)]
dic = {}
# 암호값 = 평문값 + 키값 ---> 키값 = 암호값 - 평문값
# 암호값이 26보다 커지면 26빼줌 ---> 키값이 0보다 작으면 26더해줌
for i in range(n):
    k[i] = ord(coded_text[i]) - ord(clear_text[i])
    if k[i] < 1: k[i] += 26
    k[i] = chr(ord('A') + k[i] - 1)

for i in range(1, n+1):
    if n % i == 0:
        if k[:i]*(n//i) == k:
            print(''.join(k[:i]))
            break