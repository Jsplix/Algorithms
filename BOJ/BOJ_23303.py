import sys
input = sys.stdin.readline
# [BOJ] 23303 이 문제는 D2 입니다. / 구현, 문자열
print("D2" if input().rstrip().upper().count('D2') > 0 else "unrated")