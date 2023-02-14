import sys
input = sys.stdin.readline
# [BOJ] 12891 DNA 비밀번호 / 문자열, 슬라이딩 윈도우
s, p = map(int, input().split())
dna_str = input().rstrip()
kind = list(map(int, input().split()))

# 0 - 'A', 1 - 'C', 2 - 'G', 3 - 'T'
chk = dna_str[:p]
d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for c in chk:
    d[c] += 1

answer = 0
if d['A'] >= kind[0] and d['C'] >= kind[1] and d['G'] >= kind[2] and d['T'] >= kind[3]:
    answer += 1

start = 0
end = start + p
for i in range(s-p):
    d[dna_str[start+i]] -= 1
    d[dna_str[end+i]] += 1
    if d['A'] >= kind[0] and d['C'] >= kind[1] and d['G'] >= kind[2] and d['T'] >= kind[3]:
        answer += 1

print(answer)