import sys
input = sys.stdin.readline
# [BOJ] 31216 슈퍼 소수 / 수학, 정수론, 소수 판정, 에라토스테네스의 체
p = [i for i in range(320000)]
def eratosthenes():
    p[0] = p[1] = 0

    for i in range(2, int(320000**0.5) + 1):
        if not p[i]: continue
        for j in range(i * i, 320000, i):
            p[j] = 0
    
    super_prime = []
    k = 0
    for i in range(2, 320000):
        if p[i]:
            k += 1
            if p[k]:
                super_prime.append(i)

    return super_prime

ret = eratosthenes()
for _ in range(int(input())):
    n = int(input())
    print(ret[n - 1])