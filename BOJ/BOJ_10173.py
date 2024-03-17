import sys
input = sys.stdin.readline
# [BOJ] 10173 니모를 찾아서 / 문자열
while True:
    s = input().rstrip()
    if s == 'EOI': break
    s = s.lower()
    if 'nemo' in s: print("Found")
    else: print("Missing")