import sys
input = sys.stdin.readline
# [BOJ] 17614 369 / 구현, 브루트포스
n = int(input())

result = 0
for num in range(1, n+1):
    result += str(num).count('3') + str(num).count('6') + str(num).count('9')
print(result)