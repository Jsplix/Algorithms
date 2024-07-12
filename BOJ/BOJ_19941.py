import sys
input = sys.stdin.readline
# [BOJ] 19941 햄버거 분배 / 그리디
n, k = map(int, input().split())
position = list(input().rstrip())

result = 0
for i in range(n):
    if position[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if position[j] == 'H':
                result += 1
                position[j] = 'X'
                break
print(result)