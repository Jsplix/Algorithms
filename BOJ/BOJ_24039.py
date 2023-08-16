import sys
input = sys.stdin.readline
# [BOJ] 24039 2021은 무엇이 특별할까? / 수학, 정수론, 소수 판정, 에라토스테네스의 체
Eratosthenes = [i for i in range(150)]
Eratosthenes[0], Eratosthenes[1] = 0, 0
for i in range(2, 150):
    if not Eratosthenes[i]: continue
    for j in range(i+i, 150, i):
        Eratosthenes[j] = 0

prime_num = [j for j in range(150) if Eratosthenes[j]]

answer = []
for k in range(len(prime_num)-1):
    answer.append(prime_num[k]*prime_num[k+1])

n = int(input())
for k in answer:
    if k > n:
        print(k)
        break