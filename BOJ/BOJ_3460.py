import sys
input = sys.stdin.readline
# [BOJ] 3460 이진수 / 수학, 구현
for _ in range(int(input())):
    n = bin(int(input()))
    n = n[2::][::-1]

    for i in range(len(n)):
        if n[i] == '1': print(i, end=' ')
    print()