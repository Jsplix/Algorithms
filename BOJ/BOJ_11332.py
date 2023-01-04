from math import factorial
import sys
input = sys.stdin.readline
# [BOJ] 11332 시간 초과 / 구현, 많은 조건 분기
std = {'O(N)': 1, 'O(2^N)': 2, 'O(N!)': 3, 'O(N^2)': 4, 'O(N^3)': 5}

for i in range(int(input())):
    l = list(map(str, input().split()))
    if std[l[0]] == 1:
        if int(l[1]) * int(l[2]) <= 10**8 * int(l[3]):
            print("May Pass.")
        else:
            print("TLE!")
    elif std[l[0]] == 2:
        if 2**int(l[1]) * int(l[2]) <= 10**8 * int(l[3]):
            print("May Pass.")
        else:
            print("TLE!")
    elif std[l[0]] == 3:
        if factorial(int(l[1])) * int(l[2]) <= 10**8 * int(l[3]):
            print("May Pass.")
        else:
            print("TLE!")
    elif std[l[0]] == 4:
        if int(l[1])**2 * int(l[2]) <= 10**8 * int(l[3]):
            print("May Pass.")
        else:
            print("TLE!")
    elif std[l[0]] == 5:
        if int(l[1])**3 * int(l[2]) <= 10**8 * int(l[3]):
            print("May Pass.")
        else:
            print("TLE!")