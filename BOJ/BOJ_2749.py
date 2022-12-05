import sys
input = sys.stdin.readline

# [BOJ] 2749 피보나치 수 3 / DP, 피사노 주기

# 피사노 주기 -> 피보나치 수열을 K로 modulo 연산을 할 경우 피보나치 값이 주기를 가짐
# 주기는 10^k (k > 2)일 때, 항상 15 * 10^(k - 1)의 주기를 가진다.
# 문제에서는 1,000,000로 나눈 나머지라고 했으므로 주기는 15 * 10^5 = 1,500,000 의 주기를 갖는다.
# n을 입력받고 반복문으로  피보나치 수열을 메모이제이션 할 때, for문의 범위를 (n % P) + 1 값까지로 해준다.
# 출력을 할 때도 n % P에 해당하는 index의 값을 출력한다. -> P modulo를 해주지 않으면
# 1,500,000 이상의 값이 입력되면 index error가 발생할 수 있기 때문이다.
n = int(input())
fibo = [0, 1]
P = 15 * 10**5
DIV = int(1e6)
for i in range(2, (n % P) + 1):
    fibo.append((fibo[i - 1] + fibo[i - 2]) % DIV)
print(fibo[n % P]) 