from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 14713 앵무새 / 구현, 자료 구조, 문자열, 큐
n = int(input())
text = []
cnt = 0
for i in range(n):
    text.append(list(input().split()[::-1]))
    cnt += len(text[i])
queue = deque(input().split())

while queue:
    word = queue.popleft()
    k = 0
    flag = False
    while k < n:
        if text[k] == []: k += 1; continue
        if text[k][-1] == word: 
            text[k].pop()
            flag = True
            cnt -= 1
            break
        k += 1
    if not flag: print("Impossible"); exit(0)
if not cnt: print("Possible")
else: print("Impossible")