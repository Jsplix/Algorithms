import sys
input = sys.stdin.readline
# [BOJ] 2904 수학은 너무 쉬워 / 수학, 그리디, 정수론, 소수 판정, 에라토스테네스의 체, 소인수분해
LIM = 10 ** 6 + 7
prime_number = [i for i in range(LIM)]
prime_number[1] = 0
for i in range(int(LIM ** 0.5) + 1):
    if not prime_number[i]: continue
    for j in range(i * i, LIM, i):
        prime_number[j] = 0

N = int(input())
arr = list(map(int, input().split()))

check = dict()
for i in range(N):
    val = arr[i]
    idx = 2
    while val > 1:
        if prime_number[idx] and val % idx == 0:
            val //= idx
            if idx not in check:
                check[idx] = 0
            check[idx] += 1
        else:
            idx += 1

mx, cnt = 1, 0
for k, v in check.items():
    exp = v // N
    if exp == 0: continue
    mx *= k ** exp
    
    for num in arr:
        temp = 0
        for i in range(exp):
            if num % k != 0: break
            num //= k
            temp += 1
        cnt += (exp - temp)

print(mx, cnt)