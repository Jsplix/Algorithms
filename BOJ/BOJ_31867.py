import sys
input = sys.stdin.readline
# [BOJ] 31867 홀짝홀짝 / 수학, 구현, 문자열
n = int(input())
k = input().rstrip()

d = {str(i): 0 for i in range(10)}
for x in k:
    d[x] += 1

odd_sum = d['1'] + d['3'] + d['5'] + d['7'] + d['9']
even_sum = d['0'] + d['2'] + d['4'] + d['6'] + d['8']

if odd_sum == even_sum: print(-1)
elif odd_sum > even_sum: print(1)
else: print(0)