import sys
input = sys.stdin.readline
# [BOJ] 1339 단어 수학 - 백트래킹, 그리디
n = int(input())
alphabet = [ 0 for _ in range(26) ]
word_list = []
for _ in range(n):
    word_list.append(input().rstrip())

for word in word_list:
    for i in range(len(word)):
        alphabet[ord(word[i]) - ord('A')] += 10**(len(word) - i - 1)
        # 알파벳의 위치에 10의 지수승에 대한 가중치를 저장해줌 (-> 길이가 가장 긴 단어가 가장 큰 값을 가져야하기 때문)
        # 중복된 알파벳의 경우에 대해서 '='을 하지 않고 '+=' 연산으로 처리

alphabet = list(reversed(sorted(alphabet))) 
# 내림차순 정렬을 통해서 10의 가중치가 높은 수가 가장 앞으로 오게 함
v = 0
x = 9
for i in range(len(alphabet)):
    if alphabet[i] == 0 or x == 0:
        break
    v += alphabet[i] * x # 10의 가중치가 높은 순서대로 9부터 곱해줌
    x -= 1 # 그리고 1씩 감소시켜줌

print(v)