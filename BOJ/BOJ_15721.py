import sys
input = sys.stdin.readline
# [BOJ] 15721 번데기 / 구현, 브루트 포스, 시뮬레이션
sentences = [['뻔', '데기', '뻔', '데기', '뻔'*(i+1), '데기'*(i+1)] for i in range(1, 201)]
total = 0
a = int(input()); t = int(input()); chk = int(input())

bb_cnt, dg_cnt = 0, 0
idx, full_sentences = 0, ''
for i in range(200):
    full_sentences += ''.join(sentences[i])

l_idx = 0
while True:
    if full_sentences[l_idx] == '뻔':
        l_idx += 1
        bb_cnt += 1
        if chk == 0 and bb_cnt == t: print(idx); break
    else:
        l_idx += 2
        dg_cnt += 1
        if chk == 1 and dg_cnt == t: print(idx); break
    
    idx += 1
    if idx == a: idx %= a