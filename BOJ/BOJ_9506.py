import sys
input = sys.stdin.readline
# [BOJ] 9506 약수들의 합 / 수학, 구현, 정수론
while True:
    n = int(input())
    if n == -1: break

    check = []
    for i in range(1, (n//2)+1):
        if n % i == 0: check.append(i)
    
    if sum(check) == n:
        print(n, '= ', end = '')
        print(*check, sep= ' + ')
    else:
        print(n, 'is NOT perfect.')