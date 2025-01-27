import sys
input = sys.stdin.readline
# [BOJ] 29699 Welcome to SMUPC! / 수학, 구현, 문자열, 사칙연산
d = {1: 'W', 2: 'e', 3: 'l', 4: 'c', 5: 'o', 6: 'm', 7: 'e', 8: 'T', 9: 'o',
     10: 'S', 11: 'M', 12: 'U', 13: 'P', 0: 'C'}
print(d[int(input())%14])