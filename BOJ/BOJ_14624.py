import sys
input = sys.stdin.readline
# [BOJ] 14624 전북대학교 / 구현
N = int(input())
if N % 2 == 0: print("I LOVE CBNU")
else:
    print('*' * N)
    for i in range((N + 1) // 2):
        for j in range((N // 2) - i, 0, -1): 
            print(" ", end='')
        print("*", end='')
        if i == 0: 
            print()
            continue
        for j in range(2 * i - 1): 
            print(" ", end='')
        print("*", end='\n')