import sys
import math
input = sys.stdin.readline
# [BOJ] 23048 자연수 색칠하기 / 수학, 정수론, 해 구성하기, 소수 판정, 에라토스테네스의 체
def prime_number():
    global n
    eratosthenes = [i for i in range(n+1)]
    for i in range(2, n+1):
        if not eratosthenes[i]: continue
        for j in range(i * i, n+1, i):
            eratosthenes[j] = 0

    return eratosthenes

n = int(input())
p = prime_number()

answer = [0 for _ in range(n+1)]
answer[1] = 1
clr = 2
for i in range(2, n+1):
    if p[i]: answer[i] = clr ; clr += 1
    else: 
        if not i % 2: answer[i] = 2
        else: 
            for j in range(3, int(math.sqrt(i))+1, 2):
                if i % j == 0: answer[i] = answer[j] ; break

print(len(set(answer[1:]))) 
print(*answer[1:])