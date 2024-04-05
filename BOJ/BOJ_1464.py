import sys
input = sys.stdin.readline
# [BOJ] 1464 뒤집기 3 / 자료 구조, 그리디, 덱
S = list(input().rstrip())

idx = 1
ascii = [ord(ch) for ch in S]
mn = ascii[0]

# 아스키코드 작아질때까지 진행, 작아지면 작아지기 전까지 뒤집고 작아진부분에서 또 뒤집음
while idx < len(S):
    if mn < ascii[idx]:
        idx += 1
    else:
        mn = ascii[idx]
        S[:idx] = S[:idx][::-1]
        S[:idx+1] = S[:idx+1][::-1]
        idx += 1
print(''.join(S))