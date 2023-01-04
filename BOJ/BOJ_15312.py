import sys
input = sys.stdin.readline
# [BOJ] 15312 이름 궁합 / 구현, 문자열
alphabet = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 3, 'I': 3, 'J': 2, 'K': 2, 'L': 1, 'M': 2, 
            'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}
A = input().rstrip()
B = input().rstrip()
S = ''

for i in range(len(A)):
    S += A[i]
    S += B[i]
chk = ''

for i in range(len(S) - 1):
    chk += str((alphabet[S[i]] + alphabet[S[i + 1]]) % 10)

idx = 0
chk = list(map(str, chk))
while len(chk) != 2:
    chk[idx] = (int(chk[idx]) + int(chk[idx + 1])) % 10
    idx += 1
    if idx == len(chk) - 1:
        idx = 0
        chk.pop()
print(''.join(map(str, chk)))