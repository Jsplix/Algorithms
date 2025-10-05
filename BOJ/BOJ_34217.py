import sys
input = sys.stdin.readline
# [BOJ] 34217 찾아오시는 길 / 수학, 구현, 사칙연산
a, b = map(int, input().split())
c, d = map(int, input().split())

hanyang, youngdap = a + c, b + d
if hanyang < youngdap: print("Hanyang Univ.")
elif hanyang == youngdap: print("Either")
else: print("Yongdap")