import re
import sys
input = sys.stdin.readline
# [BOJ] 2671 잠수함식별 / 문자열, 정규 표현식
bit_sound = input().rstrip()
pattern = re.compile('(100+1+|01)+')
answer = pattern.fullmatch(bit_sound)
if answer: print("SUBMARINE")
else: print("NOISE")