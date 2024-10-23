import sys
input = sys.stdin.readline
# [BOJ] 14532 보석 도둑 / 수학, 정수론, 소수 판정, 에라토스테네스의 체
k = int(input())
bags = []

def solve(x):
    for i in range(2, int(x**0.5)+1):
        while not x % i: 
            bags.append(i)
            x //= i
    
    if x != 1: bags.append(x)

solve(k)
print(len(bags))
print(*bags)