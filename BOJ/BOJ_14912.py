import sys
input = sys.stdin.readline
# [BOJ] 14912 숫자 빈도수 / 수학, 구현, 브루트포스
n, d = map(int, input().split())
num_str = ''
for i in range(1, n+1):
    num_str += str(i)
print(num_str.count(str(d)))