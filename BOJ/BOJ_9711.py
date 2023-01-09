import sys
input = sys.stdin.readline

fibo = [0 for _ in range(10001)]
fibo[1] = 1
for i in range(2, 10001):
    fibo[i] = fibo[i-1] + fibo[i-2]

for i in range(int(input())):
    p, q = map(int, input().split())
    print("Case #{0:d}: {1:d}".format(i + 1, fibo[p] % q))