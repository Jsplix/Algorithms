import sys
input = sys.stdin.readline
# [BOJ] 17176 암호해독기 / 구현, 문자열
# 시간 복잡도 개선한 코드
n = int(input())
cipherNum = [*map(int, input().split())]
plainText = input().rstrip()
text = ''

for i in range(n):
    if cipherNum[i] > 26: text += chr(cipherNum[i]+70)
    elif cipherNum[i] > 0: text += chr(cipherNum[i]+64)
    else: text += ' '
# 암호된 수를 문자로 바꾸고 문자열에 추가해준 다음 평문과 해독한 문자열을 정렬해서 같은지 확인
if sorted(text) == sorted(plainText): print('y')
else: print('n')