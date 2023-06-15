import sys
input = sys.stdin.readline
# [BOJ] 5893 17배 / 수학, 구현, 임의 정밀도, 큰 수 연산
binary = list(map(int, input().rstrip()[::-1]))

bin_to_dec = 0
for i in range(len(binary)):
    if binary[i] == 1: bin_to_dec += 2**i
print(bin(17*bin_to_dec)[2:])