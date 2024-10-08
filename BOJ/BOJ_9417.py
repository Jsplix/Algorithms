import sys
input = sys.stdin.readline
# [BOJ] 9417 최대 GCD / 수학, 브루트포스, 정수론, 유클리드 호제법
def solve(p, q):
    if q == 0:
        return p
    return solve(q, p % q)

for _ in range(int(input())):
    num = list(map(int, input().split()))
    num.sort()

    answer = 1
    for i in range(len(num)):
        temp = 1
        for j in range(len(num)):
            if i == j: continue
            temp = max(solve(num[i], num[j]), temp)
        answer = max(answer, temp)
    print(answer)