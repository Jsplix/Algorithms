import sys
input = sys.stdin.readline
# [BOJ] 25306 연속 XOR / 수학
def XOR(X):
    mod = X % 4
    if mod == 0: return X
    elif mod == 1: return 1
    elif mod == 2: return X + 1
    else: return 0

A, B = map(int, input().split())
result = XOR(B) ^ XOR(A -1)
print(result)