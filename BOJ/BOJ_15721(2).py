from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 15721 번데기 / 구현, 브루트 포스, 시뮬레이션
# 자료구조 사용 (deque를 이용한 환형 큐 풀이) / 그냥 리스트로 해도 통과하긴 함
sentences = [['뻔', '데기', '뻔', '데기', '뻔'*(i+1), '데기'*(i+1)] for i in range(1, 201)]
total = 0
a = int(input()); t = int(input()); chk = int(input())

bb_cnt, dg_cnt = 0, 0
idx, full_sentences = 0, ''
for i in range(200):
    full_sentences += ''.join(sentences[i])

l_idx = 0
queue = deque([i for i in range(a)])
l = [i for i in range(a)]    
while True:
    if full_sentences[l_idx] == '뻔':
        l_idx += 1
        bb_cnt += 1
        if chk == 0 and bb_cnt == t:
            print(queue[0])
            # print(l[0])
            break
    else:
        l_idx += 2
        dg_cnt += 1
        if chk == 1 and dg_cnt == t:
            print(queue[0])
            # print(l[0])
            break
    # l.append(l.pop(0))  
    queue.append(queue.popleft())