import sys
input = sys.stdin.readline
# [BOJ] 29728 실버와 소수는 둘다 S로 시작한다 / 수학, 구현, 에라토스테네스의 체, 자료구조, 정수론, 소수 판정, 덱
n = int(input())
s_cnt, b_cnt = 0, 0

num = [0, 0] + [i for i in range(2, n+1)]
for i in range(2, int(n**0.5)+1):
    if not num[i]: continue
    for j in range(i*i, n+1, i):
        num[j] = 0

for k in range(1, n+1):
    if num[k]:
        if not num[k-1]: b_cnt -= 1; s_cnt += 1
        s_cnt += 1
    else:
        b_cnt += 1

print(b_cnt, s_cnt)