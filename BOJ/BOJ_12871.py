from math import lcm
import sys
input = sys.stdin.readline
# [BOJ] 12871 무한 문자열 / 수학, 구현, 문자열
s = input().rstrip()
t = input().rstrip()

s_len, t_len = len(s), len(t)
x = lcm(s_len, t_len)
q1, q2 = x // s_len, x // t_len

if s*q1 == t*q2: print(1)
else: print(0)