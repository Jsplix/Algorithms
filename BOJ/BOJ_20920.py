import sys
input = sys.stdin.readline
# [BOJ] 20920 영단어 암기는 괴로워 / 자료 구조, 문자열, 정렬, 해시
n, m = map(int, input().split())
word_dic = {}
for _ in range(n):
    word = input().rstrip()
    if len(word) < m: continue
    
    if word in word_dic.keys():
        word_dic[word] += 1
    else:
        word_dic[word] = 1

answer = [(k, v) for k, v in word_dic.items()]
answer.sort(key= lambda x: (-x[1], -len(x[0]), x[0]))
for i in range(len(answer)):
    print(answer[i][0])