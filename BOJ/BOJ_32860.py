import sys
input = sys.stdin.readline
# [BOJ] 32860 수수수수퍼노바 / 수학, 구현, 사칙연산
year, seq = input().split()
result = "SN " + year

seq = int(seq)
if seq <= 26:
    seq -= 1
    result += chr(ord('A') + seq)
else:
    seq -= 26
    f = seq // 26
    s = seq % 26

    if not s: # 26 배수인 경우
        f -= 1
        s = 25
    else: 
        s -= 1
    c = {i: chr(i + ord('a')) for i in range(26)}
    result += c[f] + c[s]
print(result)