import sys
input = sys.stdin.readline
# [BOJ] 27970 OX / 수학, 애드혹
# O - 1, X - 0으로 생각하면 이진수를 뒤집어놓은 것에서 0으로 만드는 것과 같음
MOD = 10**9 + 7
s = input().rstrip()

answer = 0
for i in range(len(s)):
    if s[i] == 'O':
        answer += 2**i
    answer %= MOD
print(answer)
