import sys
input = sys.stdin.readline
# [BOJ] 25641 균형 잡힌 소떡소떡 / 구현, 문자열
n = int(input())
s = input().rstrip()

d = {'s': s.count('s'), 't': s.count('t')}
for i in range(n):
    if d['s'] == d['t']: 
        print(s[i:])
        break
    d[s[i]] -= 1