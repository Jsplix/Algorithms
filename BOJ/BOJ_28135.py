import sys
input = sys.stdin.readline
# [BOJ] 28135 Since 1973 / 구현, 문자열, 브루트포스
n = int(input())
result = 0
for i in range(n):
    str_num = str(i)
    cnt = str_num.count('50')
    if cnt: result += 1
    result += 1
print(result)