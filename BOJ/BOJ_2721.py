import sys
input = sys.stdin.readline
# [BOJ] 2721 삼각수의 합 / 수학, 구현
def total(x):
    return (x*(x+1))//2


for _ in range(int(input())):
    n = int(input())
    
    answer = 0
    for i in range(1, n+1):
        answer += (i * total(i+1))
    print(answer)