import itertools
import sys
input = sys.stdin.readline
# [BOJ] 14888 연산자 끼워넣기 / 브루트 포스
# 백트래킹을 사용하지 않고 permutations를 이용하여 해결함.
n = int(input())
num_list = list(map(int, input().split()))
oper_num = list(map(int, input().split())) # 연산자 개수 입력받음
oper = [] # 연산자 저장
for i in range(4): # 각각의 개수(값) 만큼 oper 리스트에 저장
    if i == 0:
        oper += ['+'] * oper_num[i]
    elif i == 1:
        oper += ['-'] * oper_num[i]
    elif i == 2:
        oper += ['*'] * oper_num[i]
    elif i == 3:
        oper += ['/'] * oper_num[i]
chk = []
# oper 리스트의 연산자들을 permutations를 통해서 가능한 순열을 모두 만듬
# set을 통해서 중복제거
for per in list(set(itertools.permutations(oper))): 
    v = num_list[0]
    for i in range(len(per)):
        if per[i] == '+':
            v += num_list[i + 1]
        elif per[i] == '-':
            v -= num_list[i + 1]
        elif per[i] == '*':
            v *= num_list[i + 1]
        elif per[i] == '/':
            if v < 0:
                v = abs(v) // num_list[i + 1]
                v *= -1
            else:
                v //= num_list[i + 1]
    chk.append(v)
    # 각 순열의 경우에 따라서 계산한 값을 chk 리스트에 저장
print(str(max(chk)) + '\n' + str(min(chk)))