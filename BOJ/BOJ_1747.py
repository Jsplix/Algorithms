import sys
input = sys.stdin.readline
# [BOJ] 1747 소수&팰린드롬 / 수학, 브루트포스, 정수론, 소수 판정, 에라토스테네스의 체
MX = 1003001 # 1000000 보다 크면서 가장 작은 팰린드롬 소수
def Eratosthenes():
    ret = [0, 0] + [i for i in range(2, MX+1)]
    for i in range(2, int(MX**0.5)+1):
        if not ret[i]: continue
        for j in range(i*i, MX+1, i):
            ret[j] = 0
    
    return ret

n = int(input())
sieve = Eratosthenes()

v = n
while True:
    if sieve[v]:
        temp = str(v)
        if temp == temp[::-1]:
            print(v)
            break
    v += 1