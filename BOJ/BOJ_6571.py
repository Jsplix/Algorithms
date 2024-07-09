import sys
input = sys.stdin.readline
# [BOJ] 6571 피보나치 수의 개수 / 수학, DP, 임의 정밀도, 큰 수 연산
fibo = [1, 2]

idx = 2
while True:
    if fibo[-1] > 10**100: break
    fibo.append(fibo[idx-1] + fibo[idx-2])
    idx += 1

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0: break

    answer = 0
    for i in range(len(fibo)):
        if a <= fibo[i] <= b:
            answer += 1
        elif fibo[i] > b:
            break
    print(answer)