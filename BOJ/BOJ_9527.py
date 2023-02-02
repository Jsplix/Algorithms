import sys
input = sys.stdin.readline
# [BOJ] 9527 1의 개수 세기 / 수학, 누적 합, 비트마스킹
# 10^16 ==> 약 2^55
a, b = map(int, input().split())
total = [0 for _ in range(60)] 

for i in range(1, 56):
    total[i] = 2**(i-1) + 2*total[i-1]
    # total[i] = (2**i)-1까지의 1의 개수 (2진수에서)

def solve(n):
    bin_n = bin(n)[2:]
    leng = len(bin_n)
    c = 0

    for i in range(leng):
        if bin_n[i] == '1':
            x = leng-i-1
            c += total[x]
            c += (n - 2**x + 1)
            n -= 2**x
    return c

print(solve(b)-solve(a-1))