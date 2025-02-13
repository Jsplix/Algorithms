import sys
input = sys.stdin.readline
# [BOJ] 32306 Basketball Score / 수학, 구현, 사칙연산
t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))

sm1 = t1[0] + t1[1]*2 + t1[2]*3
sm2 = t2[0] + t2[1]*2 + t2[2]*3

if sm1 == sm2: print(0)
elif sm1 > sm2: print(1)
else: print(2)