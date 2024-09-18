import sys
input = sys.stdin.readline
# [BOJ] 1788 피보나치 수의 확장 / 수학, DP
# 음수, 양수 상관없이 피보나치 수열의 절댓값은 동일함.
# 하지만, 음수의 경우 0을 제외한 짝수 인덱스 일 때는 '-'의 값이 되며, 이외는 모두 양수임
MOD = 10**9
def fibo(n):
    ret = [0, 1]

    if n == 0 or n == 1: return n
    for i in range(2, n+1):
        ret.append((ret[i-1] + ret[i-2]) % MOD)
    
    return ret[n]

n = int(input())

result = fibo(abs(n))
if n < 0:
    if not n % 2:
        print(-1, result, sep='\n')
    else:
        print(1, result, sep='\n')
else:
    if n == 0: print(0, 0, sep='\n')
    else:
        print(1, result, sep='\n')