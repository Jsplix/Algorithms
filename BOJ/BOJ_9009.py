import sys
input = sys.stdin.readline
# [BOJ] 9009 피보나치 / 수학, 그리디
fibo = [0, 1]
for i in range(2, 46):
    fibo.append(fibo[i-1] + fibo[i-2])
fibo = fibo[::-1]

for _ in range(int(input())):
    n = int(input())
    answer = []
    
    for f in fibo:
        if f <= n: 
            answer.append(f)
            n -= f

        if n == 0:
            answer.sort()
            print(*answer)
            break