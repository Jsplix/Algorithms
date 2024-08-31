import sys
from itertools import permutations
input = sys.stdin.readline
# [BOJ] 3671 산업 스파이의 편지 / 수학, 브루트포스, 정수론, 조합론, 소수 판정, 에라토스테네스의 체
MAX = 10**7
def isPrimeNum(x):
    if x == 0 or x == 1: return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0: return False
    return True

for _ in range(int(input())):
    num = input().rstrip()
    possible = set()
    for i in range(1, len(num)+1):
        for x in permutations(list(num), i):
            temp = int(''.join(x))
            if isPrimeNum(temp):
                possible.add(temp)
    print(len(possible))