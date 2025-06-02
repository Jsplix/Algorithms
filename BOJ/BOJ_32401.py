import sys
input = sys.stdin.readline
# [BOJ] 32401 ANA는 회문이야 / 구현, 문자열, 브루트포스
n = int(input())
s = input().rstrip()

result = 0
for i in range(n-2):
    for j in range(i+2, n):
        temp = s[i:j+1]
        if temp.count('A') == 2 and temp.count('N') == 1 and temp[0] == temp[-1] == 'A':
            result += 1
print(result)