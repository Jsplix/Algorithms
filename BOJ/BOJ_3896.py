import sys
input = sys.stdin.readline
# [BOJ] 3896 소수 사이 수열 / 수학, 정수론, 소수 판정, 에라토스테네스의 체
def Eratosthenes():
    sieve = [0, 0] + [1 for _ in range(2, 1299710)]
    for i in range(2, int(1299710**0.5)+1):
        if not sieve[i]: continue
        for j in range(i+i, 1299710, i):
            sieve[j] = 0
    return sieve


answer = Eratosthenes()
le = 0
for _ in range(int(input())):
    k = int(input())
    if answer[k]: # if input number(=k) is prime number ==>
        le = 0
    else: # input number(=k) in not prime number
        lp = k-1
        while True:
            if answer[lp]: break
            lp -= 1
        rp = k+1
        while True:
            if answer[rp]: break
            rp += 1
        le = rp - lp
    print(le)