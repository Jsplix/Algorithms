import sys
import re
input = sys.stdin.readline
# [BOJ] 1013 Contact / 문자열, 정규 표현식
pattern = '(100+1+|01)+'
for _ in range(int(input())):
    recv = input().rstrip()
    # re.fullmatch(pattern, string) → string에서 pattern이 있는지 확인 / 있다면 객체 반환 없다면 None
    if re.fullmatch(pattern, recv): print("YES")
    else: print("NO")