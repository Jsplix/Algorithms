import sys
input = sys.stdin.readline
# [BOJ] 6443 애너그램 / 백트래킹, 문자열
def back(idx):
    if len(chk) == len(word):
        print(''.join(chk))
        # answer.append(''.join(chk))
        return

    for i in visited:
        if visited[i]:
            chk.append(i)
            visited[i] -= 1
            back(idx + 1)
            visited[i] += 1
            chk.pop()

for _ in range(int(input())):
    chk = []
    answer = []
    word = sorted(list(map(str, input().rstrip())))
    visited = {}
    
    for c in word:
        if c in visited:
            visited[c] += 1
        else:
            visited[c] = 1

    back(0)