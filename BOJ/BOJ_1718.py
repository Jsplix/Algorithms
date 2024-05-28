import sys
input = sys.stdin.readline
# [BOJ] 1718 암호 / 구현, 문자열
plain_text = input().rstrip()
secret_key = input().rstrip()

change = ''
idx, s_idx = 0, 0
while idx < len(plain_text):
    if plain_text[idx] == ' ': 
        change += ' '
        idx += 1
        s_idx += 1
        if s_idx == len(secret_key):
            s_idx %= len(secret_key)
        continue
    chk = ord(plain_text[idx]) - ord(secret_key[s_idx])
    if chk > 0:
        change += chr(chk + ord('a') - 1) 
    else:
        change += chr(chk + 25 + ord('a'))
    
    idx += 1 ; s_idx += 1
    if s_idx == len(secret_key):
        s_idx %= len(secret_key)

print(change)