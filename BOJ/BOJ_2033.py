import sys
input = sys.stdin.readline
# [BOJ] 2033 반올림 / 수학, 구현
n = int(input())
MOD = 10
result = n
while result > MOD:
    if result % MOD >= MOD // 2:
        result += MOD
    result -= (result % MOD)
    MOD *= 10
print(result)