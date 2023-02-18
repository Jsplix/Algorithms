import sys
input = sys.stdin.readline
# [BOJ] 2312 수 복원하기 / 수학, 정수론, 소수 판정, 에라토스테네스의 체
M = int(1e5)
def Eratosthenes():
    chk = [0, 0]
    chk += [1 for _ in range(2, M+1)]
    for i in range(2, int(M**0.5)+1):
        if not chk[i]: continue
        for j in range(i+i, M+1, i):
            chk[j] = 0
    return [i for i in range(M+1) if chk[i]]

for _ in range(int(input())):
    n = int(input())
    prime = Eratosthenes()
    idx = 0
    count = {}
    while True:
        if n <= 1: break
        if n % prime[idx] == 0:
            n //= prime[idx]
            if prime[idx] not in count.keys(): count[prime[idx]] = 1
            else: count[prime[idx]] += 1
            idx = 0
        else: idx += 1

    answer = [(k, v) for (k, v) in count.items()]
    answer.sort(key=lambda x:x[0])
    for i in range(len(answer)):
        print(*answer[i])