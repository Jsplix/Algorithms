import sys
input = sys.stdin.readline
# [BOJ] 1141 접두사 / 문자열, 정렬, 그리디
n = int(input())
words = [input().rstrip() for _ in range(n)]
words.sort(key=len)

answer = 0
for i in range(n):
    flag = False
    for j in range(i+1, n):
        if words[j][:len(words[i])] == words[i]:
            flag = True
            break
    
    if not flag: answer += 1
print(answer)